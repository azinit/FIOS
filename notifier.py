import time

import FIOS.substance as substance
import FIOS.convert as convert
import FIOS.sample as smp

inspect = substance.inspect
font = smp.font
default_width = convert.cfg.Settings.width


# TODO: %s / %s %s; simplify
def result(item, flag, mode, sub='', decore=lambda x: x, general_color='',
           true_color=font.blue2, none_color=font.yellow, init=True):
    # TODO: None event
    first, second, flag = substance.init(item), substance.init(sub), substance.init(flag).property
    # input(flag)
    arrow, end = smp.objects.get("arrow"), '' if general_color else font.end
    col_main = [font.red] + [true_color] + [none_color] if not general_color else ['', '', '']
    col_sub = [font.red2] + [font.beige] + [font.yellow] if not general_color else ['', '', '']
    item = font.paint(str(first.sign + ' ')*init + str(decore(first.content)), col_main[flag], end)
    sub = font.paint(str(second.sign + ' ')*init + str(decore(second.content)), col_sub[flag], end) if sub or sub == 0 else None
    notification_dict = {
        "create": ["%s already exists!", "Created: %s", "{}Error{} occurred: %s".format(font.yellow, font.end)],
        "rename": ["Failed %s {0} %s".format(arrow), "%s {0} %s".format(arrow), "Not found: %s"],
        "delete": ["Deleting %s failed.", "Deleted: %s", "Not found: %s"],
        "clean": ["Cleaning %s failed.", "Cleaned: %s", "Not found: %s"],
        "sort": ["%s Sorting in the %s failed.", "🎩 %s Sorted: %s files ", "Sort directory: %s"],
        "move": ["Failed %s {0} %s".format(arrow), "%s {0} %s".format(arrow), "Not found: %s"],
        "open": ["Failed opening: %s", "Opened: %s", "Opening... %s"],
        "navigator": ["Incorrect path/input: %s", "Current directory: %s", "➥ %s"],
        "read": ["Input file %s not found", "Reading from: %s", "{}Error{} occurred: %s".format(font.yellow, font.end)],
        "write": ["Output file %s not found", "Writing to: %s", "{}Error{} occurred: %s".format(font.yellow, font.end)],
        "cur_dir": ["%s not found", "Directory: %s", "{}Error{} occurred: %s".format(font.yellow, font.end)]
    }
    replace = (item, sub) if sub else item
    print(general_color + notification_dict[mode][flag] % replace + font.end)


def status(tag='', pattern='', width=0, color='', delta=0):
    name = str(inspect.stack()[1+delta][3]) if not tag else tag
    pattern = '-' if not pattern else pattern
    width = default_width if not width else width
    name = convert.to_center(name.upper(), width, pattern, color)
    print(name)


def message_console(message, sub_msg='', c_pat="> ", color=font.beige, c_pat_color=font.beige, time_delay=0):
    time.sleep(time_delay)
    c_pat_color = '' if not color else c_pat_color
    print(font.paint(c_pat, c_pat_color, color) + font.paint(str(message), color, ''), str(sub_msg))


def parameters(*args, marker=smp.objects.get("element"), color=font.beige):
    if isinstance(args[0], dict):
        for key in dict(args[0]).keys():
            print(marker, key + ":", font.paint(args[0].get(key), color))

    else:
        for x in args:
            print(marker, font.paint(x, color))


def process(mode, flag, color=font.beige, pat='.'):
    color = color + font.black if color in font.backs else color
    res = ["finishing", "starting", "in process"]
    print("{} {}{}".format(font.paint(mode.capitalize(), color), res[substance.init(flag).property], pat*7))


# TODO: Upgrade Height
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
    for i, i_mode in enumerate(["create", "clean", "sort", "move", "open", "read", "write", "cur_dir"]):
        for j, i_state in enumerate([False, True, None]):
            print("{}_{}: ".format(i_mode, i_state), end=' ')
            result(item="SomeItem", flag=i_state, mode=i_mode, sub="SubItem" if i in [2, 3] and j in [0, 1] else "")
    result(item="Some", flag=True, mode="move", sub="Sub", decore=lambda x: str(x).upper())
    status(tag="SOME-TITLE", pattern='-', width=20)
    for flagg in [False, True, None]:
        process(mode="navigator", flag=flagg, color=font.beigebg, pat='.')
    for i in range(2, 5):
        print(i)
        message_box(message="Hello!", b_pat=".", b_gap=" ", b_m=i)
    message_console("Enter number: ")
    parameters(1, 2, 3)
