"""
..............................................................................................................
................................................ METHODS SUMARRY .............................................
..............................................................................................................
"""
# def key_by_value(search, dictionary):
#     for key, value in dict(dictionary).items():
#         value = [value] if not isinstance(value, list) else _to_sng(value)
#         if search in value:
#             return key
# TODO: Sync parameter?

# def key_of(src: dict, search_value):
#     for key, value in src.items():
#         if value == search_value:
#             return key
#     else:
#         return None


def are_dict(src: list):
    """ Check if all src-items are dict """
    return all(isinstance(x, dict) for x in src)


def contains(src: dict, *keys):
    """ Check if src contains all *keys """
    p = [k in src.keys() for k in keys]
    return all(p)


def contains_all(src: list, *keys):
    """ Check if all src-items contains all *keys """
    p = [contains(x, *keys) for x in src]
    return all(p)


def extract(src: dict, *keys, **kwargs):
    """ Extract all *keys properties from src to new dict """
    soft = kwargs.get("soft", False)

    if contains(src, *keys) or soft:
        data = {}
        for k in keys:                                                      # extracting
            if (True ^ soft) or contains(src, k):   data[k] = src[k]

        if len(keys) == 1 and data:                 data = data[keys[0]]    # if possible to convert to single value
        return data
    else:
        return None


def extract_all(src: list, *keys, **kwargs):
    """ Extract all*keys properties from all src-items to new items collection """
    soft = kwargs.get("soft", False)
    if are_dict(src) and (soft or contains_all(src, *keys)):
        data            = [extract(item, *keys, soft=soft) for item in src]
        if soft: data   = [item for item in data if item]
        return data
    else:
        return kwargs.get("none_case", None)


def expand(src: dict, options: dict):
    """ Add options data for src data """
    return {**src, **options}


def expand_all(src: list, options: list):
    """ Add all options-items to all src-items with matching """
    from fios.util.flist import are_uniform as __are_uniform
    if are_dict(src) and are_dict(options) and __are_uniform(src, options):
        return [expand(item, option) for item, option in zip(src, options)]
    else:
        return None


def exclude(src: dict, *properties, **kwargs):
    """
    Exclude all certain properties in object
    :param src:           object
    :param properties:    properties for exclude
    :return:              Processed object
    """
    soft = kwargs.get("soft", False)
    sync = kwargs.get("sync", False)

    if contains(src, *properties) or soft:
        data = src if sync else src.copy()
        for k in properties:
            if (True ^ soft) or contains(data, k):   data.pop(k)
        return data
    else:
        return None


def exclude_all(src: list, *properties, **kwargs):
    """
    Exclude all certain properties in list of objects
    :param src:           list of objects
    :param properties:    properties for exclude
    :return:              Excluded list
    """
    soft = kwargs.get("soft", False)
    sync = kwargs.get("sync", False)

    if are_dict(src) and (soft or contains_all(src, *properties)):
        return [exclude(item, *properties, soft=soft, sync=sync) for item in src]
    else:
        return kwargs.get("none_case", None)


def are_match(src_1: dict, src_2: dict, *keys, **kwargs):
    """
    Check if both dictionaries has similar certain key-value properties
    :param src_1:   first dict
    :param src_2:   second dict
    :param keys:    keys for matching
    :return:        Bool
    """
    soft = kwargs.get("soft", False)

    if contains(src_1, *keys) and contains(src_2, *keys):
        for k in keys:
            if src_1[k] != src_2[k]:
                return False
        else:
            return True
    else:
        return None

    # TODO: if contains options


# TODO: without search_for dict?
def index_of(src: list, search_for: dict, *keys):
    """
    Get index of dict in list
    :param src:         common_list
    :param search_for:  searching dict in list
    :param keys:        keys for matching
    :return:            -1 if not exists else index
    """

    # TODO: by all keys?
    # TODO: lowercase?
    if are_dict(src) and contains(search_for, *keys) and contains_all(src, *keys):
        for i, src_item in enumerate(src):
            if are_match(src_item, search_for, *keys):
                return i
        else:
            return -1
    else:
        return None

# TODO: COpy list of dict


def key_of(src: dict, search_for: dict, *keys):
    """
    Get key of dict in list
    :param src:         common_list
    :param search_for:  searching dict in list
    :param keys:        keys for matching
    :return:            None if not exists else key
    """
    src_list = list(src.values())
    index    = index_of(src_list, search_for, *keys)
    if index >= 0:   return list(src.keys())[index]
    else:           return None


def copy_all(src: list, **kwargs):
    """ Copy all src-items-dict """
    if are_dict(src):
        return [d.copy() for d in src]
    else:
        return None


def unique_all(src: list, *keys, **options):
    """ Get unique dict-collection form src by *keys checking """
    if are_dict(src) and contains_all(src, *keys):
        processed = []
        for i, item in enumerate(src):
            if i == 0:
                processed.append(item)
            else:
                if all(not are_match(item, item_processed, *keys) for item_processed in processed):
                    processed.append(item)
        return processed
    else:
        return None
"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    persons = [
        {"id": 0, "name": "Ilya",     "age": 19, "salary": 100000},
        {"id": 0, "name": "Ilya",   "age": 18},
        {"id": 1, "name": "Darya",    "age": 19},
        {"id": 2, "name": "Marsel",   "age": 25, "salary": 100000},
        {"id": 3, "name": "Majordom", "age": 100000},
    ]

    per_dict = {
        "feeb":                 persons[0],
        "martis-boolean":       persons[1],
        "daria":                persons[2],
        "sijava":               persons[3],
        "wow_maj":              persons[4],

    }

    e_options = [
        {"facult": "ITIS", "city": "Okt"},
        {"facult": "ITIS", "city": "Kazan"},
        {"facult": "ITIS", "city": "Mary"},
        {"facult": "ITIS", "city": "Kazan"},
        {"facult": "WOW",  "city": "FireLands"},
    ]

    objects = [
        {"name": "Majordom", "lvl": 85, "health": 100000,   "power": 500,   "location": "Fire Lands"},
        {"name": "LichKing", "lvl": 80, "health": 1000000,  "power": 1000,  "location": "Ice Crone"},
    ]

    # print(list(per_dict.keys())[0])
    # def __test__key():
    #     print(":::::::::::::::::::::key:::::::::::::::::::::")
    #     # print(key_by_value(search=".avi", dictionary=_files))
    #     print(key_of(persons[0], "Ilya"))

    def __test__extract():
        # TODO: test few similar keys
        print(":::::::::::::::::::::extract:::::::::::::::::::::")
        obj = persons[0]
        print(extract(obj, "id"))
        print(extract(obj, "name"))
        print(extract(obj, "age"))

        print("=> ALL")
        print(extract(obj, "id", "name"))
        print("=> SOFT")
        print(extract(obj, "id", "name", "salary",          soft=True))
        print(extract(persons[2], "id", "name", "salary",   soft=True))
        print(extract(persons[2], "salary",                 soft=True))
        print(extract(obj, "salary", soft=True))


    def __test__extract_all():
        # TODO: test few similar keys
        print(":::::::::::::::::::::extract_all:::::::::::::::::::::")

        print(extract_all(persons, "id"))
        print(extract_all(persons, "name"))
        print(extract_all(persons, "age"))
        print(extract_all(persons, "salary", none_case={"foo": "Custom None :)"}))
        print(extract_all(persons, "salary"))

        print("=> FEW_KEYWORDS")
        [print(x) for x in extract_all(persons, "id", "name")]
        print("=> ANY")
        [print(x) for x in extract_all(persons, "id", "name", "salary", soft=True)]
        print(extract_all(persons, "wow_lvl", soft=True))
        print(extract_all(persons, "salary",  soft=True))
        print(extract_all(persons, "salary"))


    def __test__expand():
        # TODO: test few similar keys
        print(":::::::::::::::::::::expand:::::::::::::::::::::")

        person      = persons[0]
        option      = e_options[0]

        print(expand(person, option))


    def __test__expand_all():
        # TODO: test few similar keys
        print(":::::::::::::::::::::expand_all:::::::::::::::::::::")

        [print(x) for x in expand_all(persons, e_options)]


    def __test__exclude():
        print(":::::::::::::::::::::exclude:::::::::::::::::::::")

        print(exclude(persons[2], "salary"))
        print(persons[2])

        print()

        print(exclude(persons[0], "salary"))
        print(exclude(persons[0], "salary", soft=True))
        print(exclude(objects[0], "power", "health", sync=True))
        print(objects[0])

    def __test__exclude_all():
        print(":::::::::::::::::::::exclude_all:::::::::::::::::::::")
        print(exclude_all(persons, "id"))
        print(exclude_all(persons, "name"))
        print(exclude_all(persons, "salary"))
        print(exclude_all(persons, "salary", soft=True, sync=True))
        print(persons)

    def __test__match():
        print(":::::::::::::::::::::match:::::::::::::::::::::")
        print(are_match(persons[0], persons[1], "id"))
        print(are_match(persons[0], persons[1], "name"))
        print(are_match(persons[0], persons[1], "age"))

    def __test__index_of():
        print(":::::::::::::::::::::index_of:::::::::::::::::::::")
        print(index_of(persons, persons[1], "name"))
        print(index_of(persons, objects[0], "name"))
        print(index_of(persons, objects[0], "power"))
        print(index_of(persons, objects[1], "name"))

    def __test__key_of():
        print(":::::::::::::::::::::key_of:::::::::::::::::::::")
        print(key_of(per_dict, {"name": "Marsel"}, "name"))

    def __test__unique_all():
        print(":::::::::::::::::::::unique_all:::::::::::::::::::::")
        [print(x) for x in unique_all(persons, "name")]
        print()
        [print(x) for x in unique_all(persons, "id")]
        print()
        [print(x) for x in unique_all(persons, "age")]
        [print(x) for x in unique_all(persons, "salary")]
    # ........................................................................................................
    __test__extract()
    __test__extract_all()
    __test__expand()
    __test__expand_all()
    __test__exclude()
    __test__exclude_all()
    __test__match()
    __test__index_of()
    __test__key_of()
    __test__unique_all()
