# TODO: default width?
# TODO: COLOR

DEFAULT_WIDTH = 64

"""
..............................................................................................................
................................................ METHOD SUMMARY ..............................................
..............................................................................................................
"""


def center(string: str, **kwargs):
    """ Align value with center """
    width   = kwargs.get("width", DEFAULT_WIDTH)
    symb    = kwargs.get("symb", "")
    # color   = kwargs.get("color", "")

    msg = ("{:%s^%s}" % (symb, width)).format(string)
    # return color + msg + '\33[0m'
    return msg


def float_(string: str, **kwargs):
    """ Align row with column """
    border  = kwargs.get("border", "")
    width   = kwargs.get("width", DEFAULT_WIDTH)
    # symb    = kwargs.get("symb", "")
    # color   = kwargs.get("color", "")

    msg = ("{:<%s}" % width).format(string)
    # return color + msg + border + '\33[0m'
    return msg + border


def restrain(content: str, **kwargs):
    """ Restrain {content} between two dividers with specified offset """
    offset  = kwargs.get("offset",  1)
    width   = kwargs.get("width",   DEFAULT_WIDTH)
    symb    = kwargs.get("symb",    "=")

    border_v = symb * width
    offset_v = '\n' * offset

    levels = [border_v, offset_v]
    return ''.join(levels) + content + ''.join(levels[::-1])


def put(message: str, **kwargs):
    # TODO: Margin
    # TODO: Few-rows messages
    # TODO: HTML,CSS tags?
    """ Put message in box """
    # TODO: height
    # init kwargs
    width       = kwargs.get("width",   45)
    width       = max(width, len(message) + 2)  # validate
    padding_h   = kwargs.get("padding_h", 3)
    padding_v   = kwargs.get("padding_v", 1)
    dummy       = kwargs.get("dummy", " ")

    h           = "─"
    v           = "│"
    sep         = "\r\n"
    corners     = ["┐", "┌", "└", "┘"]  # 0 - 90 - 180 - 270 - 0

    box = []

    def __width():
        return padding_h + width + padding_h

    def header():
        term = "{c_1}{t}{c_2}".format(c_1=corners[1], t=h * __width(), c_2=corners[0])
        box.append(term)

    def padding(value):
        def pv():
            term = "{v}{w}{v}".format(v=v, w=dummy * __width())
            box.append(term)

        for i in range(value): pv()

    def content():
        term = "{v}{pd}{content}{pd}{v}".format(v=v, pd= dummy * padding_h,
                                                content=center(message, symb=dummy, width=width))
        box.append(term)

    def footer():
        term = "{c_3}{t}{c_4}".format(c_3=corners[2], t=h * __width(), c_4=corners[3])
        box.append(term)

    header()
    padding(padding_v)
    content()
    padding(padding_v)
    footer()

    """
    │012345678901234567890123456790123456790123456789012│
    
    ┌───────────────────────────────────────────────────┐
    │                                                   │
    │   Serving!                                        │
    │                                                   │
    │   - Local:            http://localhost:5000       │
    │   - On Your Network:  http://192.168.1.215:5000   │
    │                                                   │
    │   Copied local address to clipboard!              │
    │                                                   │
    └───────────────────────────────────────────────────┘
    """

    return sep.join(box)


def volume(message: str, **kwargs):
    """ Make message 3D-volume """
    # TODO:
    # 3d text by symbols
    pass


def split(term: str, separator, **kwargs):
    """ Split odd part from term and return needed part """
    # TODO:
    soft        = kwargs.get("soft",    False)
    ind         = kwargs.get("ind",     -1)
    as_list     = kwargs.get("as_list", None)

    predicate   = (True ^ soft) or (separator in term)

    if predicate:
        return term.split(separator)[ind]
    else:
        return term



# TODO: pluralize?
# def verb(word, parent='get'):   # TODO:
#     # inspect
#     v = [False, False, False]
#     exc = 'bpdtnml'
#     lastchar = word[::-1].lower() if len(word) <= 3 else word[len(word):len(word) - 4:-1].lower()
#     # correct verb
#     for i in _eng['vowels']:
#         if lastchar[0] == i and i != 'y':
#             word = word[0:len(word) - 1:] + 'ing'
#             v[2] = True
#         elif lastchar[1] == i:
#             v[0] = True
#         if lastchar[2] == i:
#             v[1] = True
#     else:
#         for i in exc:
#             if lastchar[0] == i and not (v[0] and v[1]) and lastchar[1] != 'r':
#                 word += i + 'ing'
#                 break
#         else:
#             if not v[2]:
#                 word += 'ing'
#     return word


def contains(string: str, terms: list):
    """ Is string contains any term from collection """
    # TODO: Any?
    for term in terms:
        if term in string:      # equals: "string.contains(term)"
            return True
    else:
        return False


def only_letters(term: str, **options):
    """ Format string from odd characters """
    def __is_valid_gap(char: str):
        # TODO: Last char?
        return formatted[-1] != " " and char == " "

    def __is_valid_digit(char: str):
        return allow_digit and char.isdigit()

    allow_digit     = options.get("allow_digit",    False)
    gap_dot         = options.get("gap_dot",        False)
    remove_domains  = options.get("remove_domains", False)

    if remove_domains:
        from fios.enums import web
        for domain in web.get_domain_zones():
            term = term.replace(domain, " ")
    if gap_dot:     term = term.replace(".", " ")

    formatted = ""
    term      = term.strip()
    # removing odd chars
    for char in term:
        if char.isalpha() or __is_valid_gap(char) or __is_valid_digit(char):
            formatted += char

    # remove odd gap
    if formatted[-1] == " ": formatted = formatted[:-1:]
    return formatted


def similar(term_1: str, term_2: str):
    """ Compute two-terms similarity """
    from difflib import SequenceMatcher
    return SequenceMatcher(None, term_1, term_2).ratio()


def are_str(items: list):
    """ Are items strings """
    return all([isinstance(x, str) for x in items])


def similar_all(tokens: list, **options):
    """ Compute total similarity for tokens-collection """
    initial_state = options.get("initial_state",    1.0)
    skip_empty    = options.get("skip_empty",       False)

    predicate     = lambda a, b: (True ^ skip_empty) or (a != "" and b != "")
    if are_str(tokens):
        from fios.util import flist
        tokens = tokens.copy()
        tokens = flist.unify(tokens)
        tokens.sort()
        for i in range(1, len(tokens)):
            a, b = tokens[i], tokens[i - 1]
            if predicate(a, b):
                initial_state *= similar(a, b)
        return initial_state
    else:
        return None


def unique_similar_tokens(src: str, **options):
    """ Remove similar tokens from term """
    # TODO: amount?
    from fios.util import flist
    separator           = options.get("separator", " ")
    tokens              = flist.tokenize(src, separator=separator)
    processed_tokens    = flist.unique_similar_tokens(tokens, **options)
    processed_src       = separator.join(processed_tokens)
    return processed_src


def fuse(term_1: str, term_2: str, **options):
    """
    Fuse two terms by difference fusion properties:
    :save_similar => save more common term
    :save_unique  => save more unique term
    :context      => context for compute indices
    :indices      => computed indices for fusion
    :_force       => force fusion without similarity checking
    :return: new fused term
    """
    # SIMILARITY_EXACTLY    = options.get("similarity_limit", 0.86)
    SIMILARITY_LIMIT    = options.get("similarity_limit", 0.86)
    save_similar        = options.get("save_similar",  False)
    save_unique         = options.get("save_unique",   False)
    unique_indices      = options.get("indices",       [])
    context             = options.get("context",       None)
    _force              = options.get("_force",        False)
    actual_similarity   = similar(term_1, term_2)
    terms               = [term_1, term_2]

    if actual_similarity == 1.0:
        return term_1
    elif _force or actual_similarity >= SIMILARITY_LIMIT:
        if save_unique and unique_indices:
            # TODO:
            # if len(unique_values) != 2:
            #     from fios.util import flist
            #     unique_values = [0, 0]
            #     all_values = flist.compute_similarities(context)
            #     for i in range
            min_val = min(unique_indices)
            ind_min = unique_indices.index(min_val)
            return terms[ind_min]
        elif save_similar and unique_indices:
            max_val = max(unique_indices)
            ind_max = unique_indices.index(max_val)
            return terms[ind_max]
        else:
            return unique_similar_tokens(" ".join(terms))
    else:
        return None


def fuse_all(terms: list, **options):
    """
    Fuse all closes terms by options

    :param terms:                term list
    :param context:              context for terms (similarity data)
    :option save_unique:          fuse mode (save more unique value)
    :option save_similar:         fuse mode (save more common value)
    :param similarity_limit:     fuse mode (similarity limit value)
    :param sync:                 sync for terms list
    :return:
    """
    save_unique         = options.get("save_unique",        False)
    save_similar        = options.get("save_similar",       False)
    SIMILARITY_LIMIT    = options.get("similarity_limit",   0.86)
    sync                = options.get("sync",               False)
    context             = options.get("context", None)
    indices             = options.get("indices", [])
    if context or indices:
        if not sync:    terms   = terms.copy()
        if not indices: indices = [sum(x) for x in context]
        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                if save_unique ^ save_similar:
                    result = fuse(
                        terms[i], terms[j],
                        save_unique=save_unique,
                        save_similar=save_similar,
                        similarity_limit=SIMILARITY_LIMIT,
                        indices=[indices[i], indices[j]],
                    )
                    if result is not None:
                        terms[i] = terms[j] = result
                # print(result)
        return terms
    else:
        return None


def compute_distance(token_1: str, token_2: str, term: str, **options):
    """ Compute two tokens distance in term """
    tokens = only_letters(term.lower(), allow_digit=True).split(" ")

    indices_1 = [i for i, t in enumerate(tokens) if t == token_1]
    indices_2 = [j for j, t in enumerate(tokens) if t == token_2]
    if indices_1 and indices_2:
        differences = []
        for ind_1 in indices_1:
            for ind_2 in indices_2:
                differences.append(abs(ind_1 - ind_2))
        return min(differences)
    else:
        return None


"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    # TODO:
    def __test__center():
        print(":::::::::::::::::::::center:::::::::::::::::::::")
        print(center(string="SomeItem", width=20, symb='X', color='\33[36m'))

    def __test__float():
        print(":::::::::::::::::::::float:::::::::::::::::::::")
        test_set = ["292 521", "1: 123 312 321", "0: 123 51 2", "2: 123 242 424 123 123", "1: 123 323"]
        [print(float_(x, border='|', width=30)) for x in test_set]

    def __test__restrain():
        print(":::::::::::::::::::::restrain:::::::::::::::::::::")
        test_str = "Some text is there. Must be. The main thing is believe"
        print(restrain(content=test_str, offset=2, pattern='.'))

    def __test__put():
        print(":::::::::::::::::::::put:::::::::::::::::::::")
        box = put(
            message="CaseParser v.0.5",
            # width=2,
            # padding_v=1,
            dummy=" ",
        )
        print(box)

    def __test__only_letters():
        print(":::::::::::::::::::::only_letters:::::::::::::::::::::")
        term = "Ryazan, Russia - May 13, 2018: Name website on the display of PC, url -"
        print([only_letters(term)])
        term = " Ryazan, Russia - May 13, 2018: Name website on the display of PC, url -"
        print([only_letters(term)])
        term = "Illustrative Editorial of 3M Company website homepage. 3M Company logo visible on display screen."
        print([only_letters(term, allow_digit=True)])
        term = "Los Angeles, California, USA - 28 February 2019: Ctrip.com International website homepage. Ctrip.com International logo visible on display screen, Illustrative Editorial"
        print([only_letters(term, gap_dot=True)])
        print([only_letters(term, gap_dot=True, remove_domains=True)])

    def __test__contains():
        print(":::::::::::::::::::::contains:::::::::::::::::::::")
        prohibited = ["google", "yandex", "moneycontrol.com", "coinmarketcap.com"]
        # string = "www.google.com"
        string = "https://coinmarketcaep.com/currencies/factom/"
        # string = "https://coinmarketcap.com/currencies/lisk/"
        # string = "bing"
        r = contains(string, prohibited)
        print(r)

    def __test__similar():
        print(":::::::::::::::::::::similar:::::::::::::::::::::")

        print(similar("trello", "trellocom"))
        print(similar("google", "googlecom"))
        print(similar("ctrip", "ctripcom"))
        print("...")
        print(similar("enigma crypto currency co", "enigma crypto currency"))           # [2, 2] 0.94
        print(similar("cardano cryptocurrency adress", "cardano cryptocurrency"))       # [3, 1] 0.86
        print(similar("golem crypto currency", "golem crypto currency work"))           # [2, 2] 0.89
        print(similar("cdc gov", "cdc vwebsite gov"))                                   # [2, 2] 0.61
        print(similar("ryazan russia 2018 wordpress", "wordpress"))                     # [2, 2] 0.49
        print(similar("zillow", "zillow service adress"))                               # [2, 1, 1] 0.22
        print(similar("rightmove", "rightmove co uk"))                                  # [2, 2] 0.75
        print(similar("ethereum classic", "etherium"))
        print(similar("ethereum classic", "etherium adress"))
        print(similar("ethereum", "etherium adress"))
        print(similar("webster", "merriam-webster"))
        print(similar("merriam", "merriam-webster"))    # TODO: !!! (compare unions)

    def __test__fuse():
        print(":::::::::::::::::::::fuse:::::::::::::::::::::")
        print("SIMILAR")
        print(fuse("enigma crypto currency co", "enigma crypto currency"))
        print(fuse("cardano cryptocurrency adress", "cardano cryptocurrency"))
        print(fuse("golem crypto currency", "golem crypto currency work"))
        print(fuse("cdc gov", "cdc vwebsite gov"))
        print(fuse("ryazan russia 2018 wordpress", "wordpress"))
        print(fuse("zillow", "zillow service adress"))
        print("UNIQUE")
        print(fuse("enigma crypto currency co", "enigma crypto currency",       save_unique=True, indices=[1.3, 0.9]))
        print(fuse("cardano cryptocurrency adress", "cardano cryptocurrency",   save_unique=True, indices=[1.3, 0.9]))
        print(fuse("golem crypto currency", "golem crypto currency work",       save_unique=True, indices=[0.8, 1.0]))
        print(fuse("cdc gov", "cdc vwebsite gov",                               save_unique=True, indices=[0.9, 1.0]))
        print(fuse("ryazan russia 2018 wordpress", "wordpress",                 save_unique=True, indices=[1.0, 0.9]))
        print(fuse("zillow", "zillow service adress",                           save_unique=True, indices=[0.8, 0.9]))

    def __test__similar_all():
        print(":::::::::::::::::::::similar_all:::::::::::::::::::::")
        print(similar_all(["python", "python", "python"]))
        print(similar_all(["java", "javascript", "java"]))
        print(similar_all(["java", "java", "javascript"]))
        print(similar_all(["java", "javascript", "javascript"]))
        print(similar_all(["wordpress", "wordpress", "ryazan russia 2018 wordpress", "ryazan russia 2018 wordpress"]))
        print(similar_all(["wordpress", "wordpress", "ryazan russia 2018 wordpress", ""]))
        print(similar_all(["wordpress", "wordpress", "ryazan russia 2018 wordpress", ""], skip_empty=True))

    def __test__remove_similar():
        print(":::::::::::::::::::::unique_similar_tokens:::::::::::::::::::::")
        print(unique_similar_tokens("bitcoin cash cryptocurrency bch bitcoincash saply"))
        print(unique_similar_tokens("bitcoin cash cryptocurrency tablet bitcoincash"))
        print(unique_similar_tokens("washington post washingtonpost"))
        print(unique_similar_tokens("internal revenue service a irs gov"))
        print(unique_similar_tokens("ethereum classic ethereumclassic"))
        print(unique_similar_tokens("trello trello.com"))
        print(unique_similar_tokens(""))

    def __test__fuse_all():
        print(":::::::::::::::::::::fuse_all:::::::::::::::::::::")
        # print(fuse_all([1, 2, 3, 4], context="dwad"))
        context = [[1.0, 0.885, 1.0, 1.0], [0.885, 1.0, 0.885, 0.885], [1.0, 0.885, 1.0, 1.0], [1.0, 0.885, 1.0, 1.0]]
        terms   = ["bitcoin cash cryptocurrency", "bitcoin cash cryptocurrency tablet",
                   "bitcoin cash cryptocurrency", "bitcoin cash cryptocurrency"]

        context = [[1.0, 0.917, 1.0, 0.917], [0.917, 1.0, 0.917, 1.0], [1.0, 0.917, 1.0, 0.917], [0.917, 1.0, 0.917, 1.0]]
        terms   = ["kucoin crypto currency www", "kucoin crypto currency",
                   "kucoin crypto currency www", "kucoin crypto currency"]

        context = [[1.0, 0.6, 0.375, 0.375], [0.6, 1.0, 0.7, 0.7], [0.375, 0.7, 1.0, 1.0], [0.375, 0.7, 1.0, 1.0]]
        terms   = ["zillow", "zillow service",
                   "zillow real estate service", "zillow real estate service"]

        context = [[1.0, 0.7, 0.359, 0.359], [0.7, 1.0, 0.578, 0.578], [0.359, 0.578, 1.0, 1.0], [0.359, 0.578, 1.0, 1.0]]
        terms  =  ["who int", "world who int",
                   "world healt organisation who int", "world healt organisation who int"]
        [print(x) for x in context]
        print(fuse_all(terms, context=context, save_similar=True, sync=True))
        print(terms)

    def __test__distance():
        print(":::::::::::::::::::::distance:::::::::::::::::::::")
        term = "Ryazan, Russia - April 16, 2018 - Homepage of Internet Archive on the display of PC, url - archive.org."
        term = "Ryazan Russia Internet Super Zaluper Internet Archive Archive"
        print(compute_distance(token_1="archive", token_2="internet", term=term))
    # ........................................................................................................
    # __test__center()
    # __test__float()
    # __test__restrain()
    # __test__put()
    __test__only_letters()
    __test__contains()
    __test__similar()
    __test__similar_all()
    __test__remove_similar()
    __test__fuse()
    __test__fuse_all()
    __test__distance()
