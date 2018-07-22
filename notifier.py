import sys
import time
# import threading

import FIOS.substance as subst
import FIOS.convert as convert
import FIOS.sample as smp

inspect = subst.inspect
f = smp.font
default_width = convert.cfg.Settings.width


# TODO: simplify by functions; s_1, s_2, s_3 => s_1, s_2, s_3 = [generator]
def result(item, flag, mode, sub='', decore=lambda x: x, init=None,
           general_c='', i_false=f.red, i_true=f.blue2, i_none=f.yellow,
           s_false='', s_true='', s_none=''):
    col_sign = lambda name, color: f.paint(smp.objects.get(name), f.enhance(color))
    col_obj = lambda val, colors, sign: f.paint(str(sign + ' '*(len(sign) > 0)) + str(decore(subst.init(val).content)), colors[flag], end)
    def_sign = lambda val, ind: subst.init(val).sign if init[ind] is True else init[ind]

    init = [True, True] if init is None else (['', ''] if init is False else init)
    s_false = '' if not sub else (i_false if not s_false else s_false)
    s_true = '' if not sub else (f.enhance(i_true) if not s_true else s_true)
    s_none = '' if not sub else (i_none if not s_none else s_none)
    c_items, c_subs = ([i_false, i_true, i_none], [s_false, s_true, s_none]) if not general_c else (['', '', ''], ['', '', ''])
    end = '' if general_c else f.end
    sub, init[1] = (sub + ' ', init[1]) if sub or sub == 0 else ('', '')

    flag, arr = subst.init(flag).property, [col_sign(n, c) for n, c in zip(["arrow", "arrow_r", "arrow_broken"], [i_true, i_true, i_false])]
    item, sub = col_obj(item, c_items, def_sign(item, 0)), col_obj(sub, c_subs, def_sign(sub, 1))
    notification_dict = {
        "create": ["{1}{0} already exists!", "{1}Created: {0}", "{1}Error occurred: {0}"],
        "rename": ["{0} " + arr[2] + " {1}", "{0} " + arr[0] + " {1}", "Not found: {0}"],
        "delete": ["{1}Deleting {0} failed.", "{1}Deleted: {0}", "Not found: {0}"],
        "clean": ["{1}Cleaning {0} failed.", "{1}Cleaned: {0}", "Not found: {0}"],
        "sort": ["{1}Sorting in {0} failed.", "🎩 {1}Sorted: {0} files ", "Sort directory: {0}"],
        "move": ["{1} " + arr[2] + " {0}", "{1}" + arr[1] + " {0}", "Not found: {0}"],
        "open": ["Failed {1}opening: {0}", "{1}Opened: {0}", "{1}Opening... {0}"],
        "navigator": ["Incorrect {1}: {0}", "Current directory: {0}", "{1}➥ {0}"],
        "read": ["Input file {0} not found", "Reading from: {0}", "{1}Error occurred: {0}"],
        "write": ["Output file {0} not found", "Writing to: {0}", "{1}Error occurred: {0}"],
        "cur_dir": ["{1}{0} not found", "{1}Directory: {0}", "{1}Error occurred: {0}"]
    }
    print(general_c + notification_dict[mode][flag].format(item, sub) + f.end)


def status(tag='', pattern='', width=0, color='', delta=0):
    name = str(inspect.stack()[1+delta][3]) if not tag else tag
    pattern = '-' if not pattern else pattern
    width = default_width if not width else width
    name = convert.to_center(name.upper(), width, pattern, color)
    print(name)


def message_console(message, sub_msg='', c_pat="> ", color=f.beige, c_pat_color=f.beige, time_delay=0, end='\n'):
    time.sleep(time_delay)
    c_pat_color = '' if not color else c_pat_color
    print(f.paint(c_pat, c_pat_color, color) + f.paint(str(message), color, ''), str(sub_msg), end=end)


def parameters(*args, marker=smp.objects.get("element"), color=f.beige, general_color=''):
    color = general_color if general_color else color
    if isinstance(args[0], dict):
        for key in dict(args[0]).keys():
            print(general_color + marker, key + ":", f.paint(args[0].get(key), color))

    else:
        for x in args:
            print(marker, f.paint(x, color))


def process(mode, flag, color=f.beige, pat='.'):
    color = color + f.black if color in f.backs else color
    res = ["finishing", "starting", "in process"]
    print("{} {}{}".format(f.paint(mode.capitalize(), color), res[subst.init(flag).property], pat * 7))


# TODO: Upgrade Height
def message_box(message, b_pat="#", b_gap=" ", b_m=6, color='', time_delay=0):
    b_pat, b_gap, wall, length = b_pat * b_m, b_gap * b_m, b_pat * 2 + b_gap * (b_m - 2), b_m*b_m*2
    box_arc = [b_pat * b_m, b_pat * 2 + b_gap * (b_m - 2), b_pat + b_gap * (b_m - 1), wall + b_gap * (b_m - 1)]
    box_arc = list(map(lambda x: x + x[::-1], box_arc))
    message_arc = wall[:3:] + b_gap[0]*((length - len(message)) // 2 - 3)
    message = message_arc + b_gap[0]*(len(message) % 2 == 1) + message + message_arc[::-1]
    for item in box_arc + [message] + box_arc[::-1]:
        time.sleep(time_delay)
        print(color + item + f.end)


def match():
    # TODO
    # right_answer == user_answer ?
    # return red/ blue (user_answer)
    pass


# TODO: multiprocess persecond
def waiting(total_time=8):
    def _print(string):
        sys.stdout.write(string)
        sys.stdout.flush()
    print("{}⏳ ".format(f.grey), end='')
    # threading.Timer(1.0, waiting).start()
    for j in range(total_time):
        _print(".")
        time.sleep(0.25)
    print(f.end)


if __name__ == "__main__":
    waiting()
    for i, i_mode in enumerate(["create", "rename", "clean", "sort", "move", "open", "navigator", "read", "write", "cur_dir"]):
        for j, i_state in enumerate([False, True, None]):
            print("{}_{}: ".format(i_mode, i_state), end=' ')
            result(item="SomeItem", flag=i_state, mode=i_mode, sub="SubItem" if i in [1, 3, 4] and j in [0, 1] else "")
    result(item="Some", flag=True, mode="move", sub="Sub", decore=lambda x: str(x).upper())
    status(tag="SOME-TITLE", pattern='-', width=20)
    for flagg in [False, True, None]:
        process(mode="navigator", flag=flagg, color=f.beigebg, pat='.')
    for i in range(2, 5):
        print(i)
        message_box(message="Hello!", b_pat=".", b_gap=" ", b_m=i)
    message_console("Enter number: ")
    parameters(1, 2, 3)

