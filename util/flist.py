"""
..............................................................................................................
................................................ METHODS SUMMARY .............................................
..............................................................................................................
"""


def range_(gap: str, **kwargs):
    """
    Convert string "i-j" format to sorted range
        * current: i-j -> [i, i+1, ... , j-1, j]
        * update to a-z, A-Z
    """
    # parser = kwargs.get("parser")  # TODO: ? parser=lambda x: type(x)

    borders = list(map(int, gap.split('-')))
    borders.sort()
    # return [parser(x) for x in range(borders[0], borders[1] + 1)]
    return range(borders[0], borders[1] + 1)


def flat(nested: list):
    # TODO: Rewrite with rec?
    """ Convert N-dimension list to one-dimension list """
    result = []
    nested = list(nested) if type(nested) == "<class 'dict_values'>" else nested
    for i in range(len(nested)):
        while isinstance(nested[i], list):
            for sub in nested:
                result.extend(sub if isinstance(sub, list) else [sub])
            nested, result = result.copy(), []
    return nested


def fold(single: list, dimensions: int):
    # TODO: kwargs: orientation (H/V)
    insertion_list = []
    column = int(len(single) / dimensions)
    for i in range(0, dimensions):
        insertion_list.append([])
        for j in range(0, column):
            insertion_list[i].append(single[i + j * dimensions])
    return insertion_list


def sort(unsorted: list, **kwargs):
    indices         = kwargs.get("indices",         [])
    only_indices    = kwargs.get("only_indices",    False)
    reverse         = kwargs.get("reverse",         False)
    # apply           = kwargs.get("apply", True)

    if only_indices:
        import numpy
        return list(numpy.argsort(unsorted))
    else:
        if indices:
            if are_uniform(unsorted, indices) and not only_indices:
                return [unsorted[i] for i in indices]
            else:
                return None
        else:
            # TODO: apply???
            unsorted.sort()


def are_uniform(*lists: list):
    length = len(lists[0])
    return all([len(l) == length for l in lists])


"""
..............................................................................................................
................................................ REDUCERS ....................................................
..............................................................................................................
"""


def summarize(*lists: list):
    return reduce(*lists, reducer=lambda x, y: x + y)


def multiply(*lists: list):
    return reduce(*lists, reducer=lambda x, y: x * y)


def reduce(*lists: list, **kwargs):
    # init kwargs
    reducer         = kwargs.get("reducer",         lambda x, y: None)
    # validate
    a, b = lists[0][:2]
    is_reducible = type(a) == type(b) == type(reducer(a, b))
    # run
    if are_uniform(*lists) and is_reducible:
        new_list = lists[0]
        for list_ in lists[1:]: new_list = [reducer(x, y) for x, y in zip(new_list, list_)]  # TODO: Better implementation?
        return new_list
    else:
        return None


def fill_dummy(list_: list, common_length: int, **kwargs):
    dummy = kwargs.get("dummy", "")

    while len(list_) < common_length:   list_.append(dummy)
    return list_


"""
..............................................................................................................
................................................ MATCHES .....................................................
..............................................................................................................
"""


def match(src: list, states: list, **kwargs):
    def must_excluded(s):
        return int(s) == exclude_state

    dummy = kwargs.get("dummy", None)
    exclude_state = kwargs.get("exclude_state", 0)
    if dummy is None:
        return [x for x, state in zip(src, states) if not must_excluded(state)]
    else:
        return [(x if not must_excluded(state) else dummy) for x, state in zip(src, states)]


def frequency_vector(src: list, keys: list):
    return [src.count(key) for key in keys]


# TODO: Compare_Table
# src       filter_1          filter_2        filter_3
# src_1     filter_1(src_1)     ...             ...
# src_n     filter_1(src_n)     ...             ...
"""
..............................................................................................................
................................................ STRING ......................................................
..............................................................................................................
"""


def lower(tokens: list):
    """ List to lower """
    return list(map(lambda x: str(x).lower(), tokens))


"""
..............................................................................................................
................................................ TESTS  ......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    list_1 = [1, 2, 3]
    list_2 = [0, -1, 1]
    list_3 = [1, 1, 1]
    list_4 = [1, -1, 2]
    list_5 = [1, 0, 1, 2]
    list_6 = [1, 0, 1]
    list_7 = [1, 2, 3, 4, 5, 6]
    list_8 = [0, 0, 1, 0, 1, 0]

    def __show__sets():
        args = [
            list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8
        ]
        for i in range(len(args)): print("list_%d" % (i + 1), args[i])

    def __test__range():
        print(":::::::::::::::::::::range:::::::::::::::::::::")
        print(range_(gap="1-5", parser=int))
        print(range_(gap="5-1", parser=str))

    def __test__flat():
        print(":::::::::::::::::::::flat:::::::::::::::::::::")
        test_set_1 = [
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            [7, 8, 9]
        ]

        test_set_2 = [
            1,
            23,
            [5, 6, 7],
            16,
        ]
        print(flat(nested=test_set_1))
        print(flat(nested=test_set_2))

    def __test__fold():
        print(":::::::::::::::::::::fold:::::::::::::::::::::")
        test_sets = [
            [x for x in range(0, 100)],
        ]

        [print(x) for x in fold(single=test_sets[0], dimensions=10)]

    def __test__summarize():
        print(":::::::::::::::::::::summarize:::::::::::::::::::::")

        sum_list = summarize(list_1, list_2, list_3, list_4)        # [3, 1, 7]
        print(sum_list)

    def __test__multiply():
        print(":::::::::::::::::::::multiply:::::::::::::::::::::")
        print(multiply(list_1, list_1, list_1, list_1))             # [1, 16, 81]
        print(multiply(list_1, list_6))                             # [1, 0, 3]
        print(multiply(list_5, list_6))                             # None
        print(multiply(list_7, list_8))                             # [0, 0, 3, 0, 5, 0]


    def __test__reduce():
        print(":::::::::::::::::::::reduce:::::::::::::::::::::")

        reducer = lambda x, y: x ** y
        print(reduce(list_1, list_4, reducer=reducer))              # [1, 0.5, 9]


    def __test__match():
        print(":::::::::::::::::::::match:::::::::::::::::::::")
        print(match(src=list_7, states=list_8))                     # [3, 5]
        print(match(src=list_1, states=list_3))                     # [1, 2, 3]
        print(match(src=list_1, states=list_6))                     # [1, 3]
        print(match(src=list_1, states=list_6, dummy="*"))          # [1, '*', 3]
        print(match(src=list_1, states=list_1))                     # [1, 2, 3]
        print(match(src=list_1, states=list_6, exclude_state=1))    # [2]


    def __test__vector():
        print(":::::::::::::::::::::vector:::::::::::::::::::::")
        print(frequency_vector(src=list_3, keys=list_1))            # [3, 0, 0]
        print(frequency_vector(src=list_1, keys=list_7))            # [1, 1, 1, 0, 0, 0]


    __show__sets()
    __test__range()
    __test__flat()
    __test__fold()
    __test__summarize()
    __test__multiply()
    __test__reduce()
    __test__match()
    __test__vector()
