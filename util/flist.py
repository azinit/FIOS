"""
..............................................................................................................
................................................ METHODS SUMMARY .............................................
..............................................................................................................
"""


def apply_all(items: list, func):
    """ Apply func for all items in collection """
    results = [func(item) for item in items]
    return results


def are(items: list, predicator):
    # TODO:
    pass


def unify(tokens: list, **kwargs):
    """ Get unified tokens-collection """
    # TODO: KWARGS - similarity procent?
    return list(set(tokens))


def unified_size(tokens: list):
    """ Get size of unified tokens-collection """
    return len(unify(tokens))


def count(tokens: list, **options):
    """ Count tokens """
    separately = options.get("separately", False)
    counters = {}
    for token in tokens:
        if token not in counters.keys():    counters[token] = 1
        else:                               counters[token] += 1

    if separately:
        return [*counters.keys()], [*counters.values()]
    else:
        return counters


# TODO: CLEAR? (by prohibited)
def filter_(tokens: list, prohibited: list):
    """ Filter tokens from prohibited-items """
    return [x for x in tokens if x not in prohibited]


def tokenize(term: str, **kwargs):
    """ Tokenize term by separator """
    separator = kwargs.get("separator", " ")
    return term.split(separator)


def tokenize_all(terms: list, **kwargs):
    """ Tokenize all terms """
    separator = kwargs.get("separator", " ")
    tokens = []
    [tokens.extend(tokenize(t, separator=separator)) for t in terms]
    return tokens


def order(tokens: list, example_tokens: list, **options):
    """ Order tokens-collection under example-term-tokens """
    def is_valid_stop_word(_token_):
        stop_word = options.get("stop_word", False)
        return stop_word and _token_ == stop_word
    ordered_tokens = []
    for e_token in example_tokens:
        # if token in term and token not in prohibited and token not in final_term:
        if is_valid_stop_word(e_token):                             break
        if e_token in tokens and e_token not in ordered_tokens:     ordered_tokens.append(e_token)
    return ordered_tokens


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
    """ Convert N-dimension list to one-dimension list """
    # TODO: Rewrite with rec?
    result = []
    nested = list(nested) if type(nested) == "<class 'dict_values'>" else nested
    for i in range(len(nested)):
        while isinstance(nested[i], list):
            for sub in nested:
                result.extend(sub if isinstance(sub, list) else [sub])
            nested, result = result.copy(), []
    return nested


def fold(single: list, dimensions: int):
    """ Fold single-dimension list to new N-dimension list """
    # TODO: not all items
    # TODO: kwargs: orientation (H/V)
    insertion_list = []
    column = int(len(single) / dimensions)
    for i in range(0, dimensions):
        insertion_list.append([])
        for j in range(0, column):
            insertion_list[i].append(single[i + j * dimensions])
    return insertion_list


def sort(unsorted: list, **kwargs):
    """
    Sort unsorted list
    => get indices_sort => for future sort
    => sort by indices  => for sync data
    => simple sort      => ...
    """
    # TODO: reverse
    indices         = kwargs.get("indices",         [])
    only_indices    = kwargs.get("only_indices",    False)
    reverse         = kwargs.get("reverse",         False)
    soft            = kwargs.get("soft",            False)
    # apply           = kwargs.get("apply", True)

    if only_indices:
        import numpy
        indices = list(numpy.argsort(unsorted))
        if reverse: indices = indices[::-1]
        return indices
    else:
        if indices:
            if (soft or are_uniform(unsorted, indices)) and not only_indices:
                return [unsorted[i] for i in indices]
            else:
                return None
        else:
            # TODO: apply???
            unsorted.sort()


def sort_group(sample: list, lists_to_sort: list, **options):
    """
    indices....
    terms           = sort(terms, indices=indices, soft=soft)
    priorities      = sort(priorities, indices=indices, soft=soft)
    sim_indices     = sort(sim_indices, indices=indices, soft=soft)
    =>
    sort_by
    :param sample:
    :param lists_to_sort:
    :param options:
    :return:
    """
    reverse         = options.get("reverse", False)
    soft            = options.get("soft",    False)

    indices         = sort(sample, only_indices=True, reverse=reverse)

    sorted_lists = []
    for i in range(len(lists_to_sort)):
        sorted_list = sort(lists_to_sort[i], indices=indices, soft=soft)
        sorted_lists.append(sorted_list)
    return sorted_lists


def are_uniform(*lists: list):
    """ Are all lists has similar sizes """
    # TODO: dimension?
    length = len(lists[0])
    return all([len(l) == length for l in lists])

"""
..............................................................................................................
................................................ REDUCERS ....................................................
..............................................................................................................
"""


def summarize(*lists: list):
    """ Summarize lists item-by-item """
    return reduce(*lists, reducer=lambda x, y: x + y)


def multiply(*lists: list):
    """ Multiply lists item-by-item """
    return reduce(*lists, reducer=lambda x, y: x * y)


def reduce(*lists: list, **kwargs):
    """ Reduce lists with some function and memory medium state """
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


def fill_dummy(tokens: list, common_length: int, **kwargs):
    """ Fill tokens-collection by dummy before achieve common_length """
    dummy = kwargs.get("dummy", "")

    while len(tokens) < common_length:   tokens.append(dummy)
    return tokens


"""
..............................................................................................................
................................................ MATCHES .....................................................
..............................................................................................................
"""


def match(tokens: list, states: list, **kwargs):
    """
    Match tokens with states
    if state == exclude_state:  not add token / dummy
    else:                       add token
    """
    def must_excluded(s):
        return int(s) == exclude_state

    dummy           = kwargs.get("dummy", None)
    exclude_state   = kwargs.get("exclude_state", 0)
    if dummy is None:   return [(x)                                        for x, state in zip(tokens, states) if not must_excluded(state)]
    else:               return [(x if not must_excluded(state) else dummy) for x, state in zip(tokens, states)]


def frequency_vector(src: list, keys: list):
    """ Get frequency vector from src iter keys """
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
    """ Convert list to lower """
    return list(map(lambda x: str(x).lower(), tokens))


"""
..............................................................................................................
................................................ ANALYZE .....................................................
..............................................................................................................
"""


def compute_similarities(terms: list, **options):
    """ Compute similarities matrix (data) for terms """
    # TODO: optimize (diagonal matrix)
    # ["zillow", "zillow service adress", "zillow real estate service", "zillow real estate service"]]
    round_to = options.get("round_to", 3)
    from fios.util import fstring
    if fstring.are_str(terms):
        size = len(terms)
        sim_matrix = [x[:] for x in [[-1] * size] * size]
        for i, t_a in enumerate(terms):
            for j, t_b in enumerate(terms):
                if sim_matrix[i][j] == -1:
                    sim_matrix[i][j] = sim_matrix[j][i] = round(fstring.similar(t_a, t_b), round_to)
                    # similarity = [fstring.similar(t_a, t_b) for j, t_b in enumerate(src) if i != j]
            # similarity = [round(fstring.similar(t_a, t_b), 3) for j, t_b in enumerate(src)]
            # print(sum(similarity))
        return sim_matrix
    else:
        return None


def compute_differences(src: list, **options):
    """
    Compute differences from values
    !!! Specified for math analyze
    """

    # TODO: separate
    def are_num(values :list):
        return all([isinstance(x, int) or isinstance(x, float) for x in values])

    sort_src        = options.get("sort_src",    True)
    sort_res        = options.get("sort_result", False)
    reverse         = options.get("reverse",     False)
    extend_last     = options.get("extend_last", False)
    round_to        = options.get("round_to",    False)
    if are_num(src):
        src = src.copy()
        if sort_src:    src.sort()
        if reverse:     src.reverse()

        differences  =  [src[i - 1] - src[i] for i in range(1, len(src))]

        if round_to:    differences = [round(d, round_to) for d in differences]
        if extend_last: differences.append(0)
        if sort_res:    differences.sort()
        return differences
    else:
        return None


def unique_similar_tokens(tokens: list, **options):
    """ Remove similar tokens from tokens-collection """
    from fios.util.fstring import similar

    similarity_limit    = options.get("similarity_limit", 0.65)
    processed_tokens    = []
    tokens              = flat(tokens)
    # similarities = []
    for token in tokens:
        for p_token in processed_tokens:
            sim = similar(token, p_token)
            # similarities.append(sim)
            # print(token.ljust(16), p_token.ljust(16), similarities[-1])
            if sim >= similarity_limit:
                break
        else:
            processed_tokens.append(token)
            # continue

    return processed_tokens
    # print(max(similarities))
"""
..............................................................................................................
................................................ TESTS  ......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    # TODO: Test logic?
    #   test(actual, expected, thread)
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

    def __test__filter():
        print(":::::::::::::::::::::filter:::::::::::::::::::::")
        print(filter_(tokens=list_7, prohibited=list_1))

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

        [print(x) for x in fold(single=test_sets[0], dimensions=4)]

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
        print(match(tokens=list_7, states=list_8))                     # [3, 5]
        print(match(tokens=list_1, states=list_3))                     # [1, 2, 3]
        print(match(tokens=list_1, states=list_6))                     # [1, 3]
        print(match(tokens=list_1, states=list_6, dummy="*"))          # [1, '*', 3]
        print(match(tokens=list_1, states=list_1))                     # [1, 2, 3]
        print(match(tokens=list_1, states=list_6, exclude_state=1))    # [2]


    def __test__vector():
        print(":::::::::::::::::::::vector:::::::::::::::::::::")
        print(frequency_vector(src=list_3, keys=list_1))            # [3, 0, 0]
        print(frequency_vector(src=list_1, keys=list_7))            # [1, 1, 1, 0, 0, 0]

    def __test__differences():
        print(":::::::::::::::::::::differences:::::::::::::::::::::")
        print(compute_differences([1.0, 0.8, 0.5, 0.3, 0.2, 0.15, 0.1], reverse=True, sort_result=True, round_to=3))

    def __test__unique_priorities():
        print(":::::::::::::::::::::unique_priorities:::::::::::::::::::::")
        testset = ["etherium", "etherium", "etherium", "etherium classic"]
        print(count(testset))

    def __test__matching():
        print(":::::::::::::::::::::matching:::::::::::::::::::::")
        # testset = ["zillow", "zillow service adress", "zillow real estate service"]
        testset = ["zillow", "zillow service adress", "zillow real estate service", "zillow real estate service"]
        # testset = ["zillow", "zillow a", "zillow real estate service", "zillow real estate service"]
        # testset = ["ethereum", "ethereum adress", "ethereum classic", "ethereum classic"]
        [print(x) for x in compute_similarities(testset)]

    def __test__sort_by():
        print(":::::::::::::::::::::sort_by:::::::::::::::::::::")
        example = [5, 4, 2, 3, 1]
        list_9  = ["a", "b", "c", "d", "e"]
        list_10 = ["geforce", "intel", "amd", "nvidia", "omen"]
        data = sort_group(example, [list_8, list_9, example, list_7, list_10], soft=True, reverse=True)
        [print(x) for x in data]

    # ........................................................................................................
    __show__sets()
    __test__filter()
    __test__range()
    __test__flat()
    __test__fold()
    __test__summarize()
    __test__multiply()
    __test__reduce()
    __test__match()
    __test__vector()
    __test__differences()
    __test__unique_priorities()
    __test__matching()
    __test__sort_by()
