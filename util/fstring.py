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
    # TODO:
    # 3d text by symbols
    pass

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
    for term in terms:
        if term in string:      # equals: "string.contains(term)"
            return True
    else:
        return False


def only_letters(term: str):
    """ Format string from odd characters """
    def __is_valid_gap(char):
        # TODO: Last char?
        return formatted[-1] != " " and char == " "

    formatted = ""

    # removing odd chars
    for char in term:
        if char.isalpha() or __is_valid_gap(char):
            formatted += char

    # remove odd gap
    if formatted[-1] == " ": formatted = formatted[:-1:]
    return formatted


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
        term = only_letters(term)
        print([term])

    def __test__contain():
        print(":::::::::::::::::::::contain:::::::::::::::::::::")
        prohibited = ["google", "yandex", "moneycontrol.com", "coinmarketcap.com"]
        # string = "www.google.com"
        string = "https://coinmarketcaep.com/currencies/factom/"
        # string = "https://coinmarketcap.com/currencies/lisk/"
        # string = "bing"
        r = contain(string, prohibited)
        print(r)

    # __test__center()
    # __test__float()
    # __test__restrain()
    __test__put()
    __test__only_letters()
    __test__contain()
