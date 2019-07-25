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


def extract(src: list, *keys: str):
    is_dict         = map(lambda x: isinstance(x, dict),    src)
    contains_key    = map(lambda x: key in x.keys(),        src)

    if all(is_dict) and all(contains_key):
        results = []
        for item in src: results.append(item[key])
        return results
    else:
        return None


"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    def __test__key():
        print(":::::::::::::::::::::key:::::::::::::::::::::")
        # print(key_by_value(search=".avi", dictionary=_files))

    def __test__extract():
        print(":::::::::::::::::::::extract:::::::::::::::::::::")
        objects = [
            {"id": 0,   "name": "Ilya", "age": 19},
            {"id": 1,   "name": "Darya", "age": 17},
            {"id": 2,   "name": "Marsel", "age": 25},
        ]

        print(extract(objects, "id"))
        print(extract(objects, "name"))
        print(extract(objects, "age"))

    __test__extract()