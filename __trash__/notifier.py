import sys
import time
import inspect
# import threading

import FIOS.font as _f
from FIOS.cfg import Settings as _Settings
from FIOS.sample import objects as _obj
from FIOS.substance import init as _init
from FIOS.convert import to_center as _to_c

default_width = _Settings.width
_fl = 2

# TODO: simplify by functions; s_1, s_2, s_3 => s_1, s_2, s_3 = [generator]; ¯\_(ツ)_/¯ case (str = [nothing to sort, exception , .. ]); ljust
def result(item, flag, mode, sub='', decore=lambda x: x, init=None,
           general_c='', i_false=_f.red, i_true=_f.blue, i_none=_f.yellow,
           s_false=_f.red, s_true=_f.blue2, s_none=_f.yellow, end='\n', fl=_fl):
    """ Write result of process in console """
    def _col_sign(name, color):
        """ Colorize symbol """
        return _f.paint(_obj.get(name), _f.enhance(color))

    def _col_obj(val, colors, sign):
        """ Colorize item """
        return _f.paint(str(sign + ' ' * (len(sign) > 0)) + str(decore(val)), colors[flag], c_end)

    def _get_sign(val, ind):
        """ Init sign """
        return _init(val, fl=fl).sign if init[ind] is True else init[ind]
    """ Download signs from sample """
    flag, sign = _init(flag, fl=fl).property, []
    for n, c in zip(["arrow", "arrow_r", "arrow_broken", "flag", "flag"], [i_true, i_true, i_false, i_true, i_none]):
        sign.append(_col_sign(n, c))

    """ <init> init cases """
    if init is None:
        init = (True, True)
    elif init is False:
        init = ('', '')
    """ <sub> init cases """
    if sub or sub == 0:
        sub += ' '
    else:
        init = (init[0], '')
        s_false, s_true, s_none = '', '', ''
    """ <general_c> init cases """
    if general_c:
        c_items, c_subs, c_end = ['', '', ''], ['', '', ''], ''
    else:
        c_items, c_subs, c_end = [i_false, i_true, i_none], [s_false, s_true, s_none], _f.end

    """ Colorize items """
    item = _col_obj(item, c_items, _get_sign(item, 0))
    sub = _col_obj(sub, c_subs, _get_sign(sub, 1))
    notification_dict = {
        "create":       ["{1}{0} already exists!",      "{1}Created: {0}",           "{1}Error occurred: {0}"],
        "rename":       ["{0} " + sign[2] + " {1}",     "{0} " + sign[0] + " {1}",   "Not found: {0}"],
        "delete":       ["{1}Deleting {0} failed.",     "{1}Deleted: {0}",           "Not found: {0}"],
        "clean":        ["{1}Cleaning {0} failed.",     "{1}Cleaned: {0}",           "Not found: {0}"],
        "sort":         ["{1}Sorting in {0} failed.",   "🎩 {1}Sorted: {0} files ",  "Sort directory: {0}"],
        "move":         ["{1} " + sign[2] + " {0}",     "{1} " + sign[1] + " {0}",   "Not found: {0} {1}"],
        "index":        [sign[2] + " : {0}",            sign[3] + " : {0}",          sign[4] + " : {0}"],
        "open":         ["Failed {1}opening: {0}",      "{1}Opened: {0}",            "{1}Opening... {0}"],
        "navigator":    ["Incorrect {1}: {0}",          "Current directory: {0}",    "{1}➥ {0}"],
        "read":         ["Input file {0} not found",    "Reading from: {0}",         "{1}Error occurred: {0}"],
        "write":        ["Output file {0} not found",   "Writing to: {0}",           "{1}Error occurred: {0}"],
        "cur_dir":      ["{1}{0} not found",            "{1}Directory: {0}",         "{1}{0}"]
    }
    print(general_c + notification_dict[mode][flag].format(item, sub) + c_end, end=end)


def status(tag='', pattern='-', width=default_width, color='', delta=0):
    """ Write status of method, process in console """
    name = str(inspect.stack()[1+delta][3]) if not tag else tag
    name = _to_c(name.upper(), width, pattern, color)
    print(name)


def message_console(message, sub_msg='', c_pat=">> ", color=_f.beige, c_pat_color=_f.beige, time_delay=0, end=_f.end+'\n'):
    """ Write some message in console """
    time.sleep(time_delay)
    c_pat_color = '' if not color else c_pat_color
    print(_f.paint(c_pat, c_pat_color, color) + _f.paint(str(message), color, ''), str(sub_msg), end=end)


def parameters(*args, marker=_obj.get("element"), color=_f.beige, general_color='', end='\n'):
    """ Write list of parameters in console """
    color = general_color if general_color else color
    if isinstance(args[0], dict):
        for key in dict(args[0]).keys():
            print(general_color + marker, key + ":", _f.paint(args[0].get(key), color), end=end)

    else:
        for x in args:
            print(marker, _f.paint(x, color), end=end)
    print() if end.count('\n') == 0 else None


def process(mode, flag, color=_f.beige, pat='.', fl=_fl):
    """ Write step of process in console """
    color = color + _f.black if color in _f.backs else color
    res = ["finishing", "starting", "in process"]
    print("{} {}{}".format(_f.paint(mode.capitalize(), color), res[_init(flag, fl=fl).property], pat * 7))


# TODO: Upgrade Height
def message_box(message, b_pat="#", b_gap=" ", b_m=6, color='', time_delay=0):
    """ Write message_box in console """
    b_pat, b_gap, wall, length = b_pat * b_m, b_gap * b_m, b_pat * 2 + b_gap * (b_m - 2), b_m*b_m*2
    box_arc = [b_pat * b_m, b_pat * 2 + b_gap * (b_m - 2), b_pat + b_gap * (b_m - 1), wall + b_gap * (b_m - 1)]
    box_arc = list(map(lambda x: x + x[::-1], box_arc))
    message_arc = wall[:3:] + b_gap[0]*((length - len(message)) // 2 - 3)
    message = message_arc + b_gap[0]*(len(message) % 2 == 1) + message + message_arc[::-1]
    for item in box_arc + [message] + box_arc[::-1]:
        time.sleep(time_delay)
        print(color + item + _f.end)


def match():
    # TODO
    # right_answer == user_answer ?
    # return red/ blue (user_answer)
    pass


# TODO: multiprocess persecond
def waiting(total_time=8, end='\n'):
    def _print(string):
        sys.stdout.write(string)
        sys.stdout.flush()
    print("{}⏳ ".format(_f.grey), end='')
    # threading.Timer(1.0, waiting).start()
    for j in range(total_time):
        _print(".")
        time.sleep(0.25)
    print(_f.end, end=end)


if __name__ == "__main__":
    waiting()
    for i, mode_i in enumerate(["create", "rename", "clean", "sort", "move", "open", "navigator", "read", "write", "cur_dir", "index"]):
        for j, state_i in enumerate([False, True, None]):
            length = 25 - (len(mode_i) + 1 + len(str(state_i)) + 1)
            print("{}_{}:".format(mode_i, state_i), ' '*length,  end=' ')
            result(item="SomeItem", flag=state_i, mode=mode_i, sub="SubItem" if i in [1, 3, 4] and j in [0, 1] else "")

    result(item="Some", flag=True, mode="move", sub="Sub", decore=lambda x: str(x).upper())
    status(tag="SOME-TITLE", pattern='-', width=20)

    for flag_i in [False, True, None]:
        process(mode="navigator", flag=flag_i, color=_f.beigebg, pat='.')

    for i in range(2, 5):
        print(i)
        message_box(message="Hello!", b_pat=".", b_gap=" ", b_m=i)
    message_console("Enter number: ")
    parameters(1, 2, 3, end=' ')
    parameters(1, 2, 3)
    parameters(1, 2, 3, end=' ')
