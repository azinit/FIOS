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

"""
..............................................................................................................
................................................ TESTS  ......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    def __test__range():
        print(":::range:::")
        print(range_(gap="1-5", parser=int))
        print(range_(gap="5-1", parser=str))

    def __test__flat():
        print(":::flat:::")
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
        print(":::fold:::")
        test_sets = [
            [x for x in range(0, 100)],
        ]

        [print(x) for x in fold(single=test_sets[0], dimensions=10)]

    __test__range()
    __test__flat()
    __test__fold()