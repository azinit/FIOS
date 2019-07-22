# TODO: default width?
# TODO: COLOR

DEFAULT_WIDTH = 64


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


def put(content: str, **kwargs):
    # TODO:
    """
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


if __name__ == '__main__':
    # TODO:
    def __test__center():
        print(":::center:::")
        print(center(string="SomeItem", width=20, symb='X', color='\33[36m'))

    def __test__float():
        print(":::float:::")
        test_set = ["292 521", "1: 123 312 321", "0: 123 51 2", "2: 123 242 424 123 123", "1: 123 323"]
        [print(float_(x, border='|', width=30)) for x in test_set]

    def __test__restrain():
        print(":::restrain:::")
        test_str = "Some text is there. Must be. The main thing is believe"
        print(restrain(content=test_str, offset=2, pattern='.'))

    __test__center()
    __test__float()
    __test__restrain()
