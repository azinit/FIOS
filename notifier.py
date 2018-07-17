import inspect
import time

import FIOS.font as font
import FIOS.convert as convert

default_width = convert.sample.width


def result(item, state, mode):
    # TODO
    # None event
    sign, col = '13F', [font.red] + [font.blue2] + [font.end]
    mdd = {
        'create': ['13F already exists!', 'Created: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'clean': ['Cleaning 13F failed.', 'Cleaned: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'sort': ['Sorting the 13F failed.', 'Sorted: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'move': ['empty', 'empty', 'empty'],
        'read': ['Input file 13F not found', 'Reading from: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'write': ['Output file 13F not found', 'Writing to: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'cur_dir': ['13F not found', 'Directory: 13F', '{}Error{} occurred'.format(font.yellow, font.end)]
    }
    print(mdd[mode][2] if state is None else mdd[mode][state].replace(sign, str(col[state] + item + col[2])))


def status(tag='', pattern='', width=0, color=''):
    name = str(inspect.stack()[1][3]) if not tag else tag
    pattern = '-' if not pattern else pattern
    width = default_width if not width else width
    name = convert.to_center(name.upper(), width, pattern, color)
    print(name)


def message_console(message, c_pat="> ", color='', time_delay=0):
    time.sleep(time_delay)
    print(font.paint(c_pat + message, color))


def parameters(*args, marker=convert.sample.objects.get("file0"), color=font.beige):
    if isinstance(args[0], dict):
        for key in dict(args[0]).keys():
            print(marker, key + ":", font.paint(args[0].get(key), color))

    else:
        for x in args:
            print(marker, font.paint(x, color))


def process():
    pass


# TODO # Upgrade Height
def message_box(message, b_pat="#", b_gap=" ", b_m=6, color='', time_delay=0):
    b_pat, b_gap, wall, length = b_pat * b_m, b_gap * b_m, b_pat * 2 + b_gap * (b_m - 2), b_m*b_m*2
    box_arc = [b_pat * b_m, b_pat * 2 + b_gap * (b_m - 2), b_pat + b_gap * (b_m - 1), wall + b_gap * (b_m - 1)]
    box_arc = list(map(lambda x: x + x[::-1], box_arc))
    message_arc = wall[:3:] + b_gap[0]*((length - len(message)) // 2 - 3)
    message = message_arc + b_gap[0]*(len(message) % 2 == 1) + message + message_arc[::-1]
    for item in box_arc + [message] + box_arc[::-1]:
        time.sleep(time_delay)
        print(color + item + font.end)


def match():
    # TODO
    # right_answer == user_answer ?
    # return red/ blue (user_answer)
    pass


if __name__ == "__main__":
    for i_mode in ["create", "clean", "sort", "move", "read", "write", "cur_dir"]:
        for i_state in [False, True, None]:
            print("{}_{}: ".format(i_mode, i_state), end=' ')
            result(item="SomeItem", state=i_state, mode=i_mode)
    status(tag="SOME-TITLE", pattern='-', width=20)
    for i in range(2, 5):
        print(i)
        message_box(message="Hello!", b_pat=".", b_gap=" ", b_m=i)
    message_console("Enter number: ")
    parameters(1, 2, 3)
