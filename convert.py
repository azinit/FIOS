import datetime

import FIOS.font as font
import FIOS.sample as sample

sections = ['Common', 'Aligning', 'Time']
functions = [['to_graphic_path', 'from_gap', 'to_simple_list'], ['to_center', 'to_rows'], ['to_datetime', 'to_hms', 'to_seconds']]
default_width = sample.width


# =====   Common   ===== #
def to_graphic_path(path):
    return path.replace('\\', ' ⟩⟩ ')


def to_divided(content, offset=1, pattern="="):
    return pattern * default_width + '\n' * offset + content + '\n' * offset + pattern * default_width


def to_interval(gap, parser=lambda x: type(x)):
    # current: i-j -> [i, i+1, ... , j-1, j]
    # update to a-z, A-Z
    borders = list(map(int, gap.split('-')))
    borders.sort()
    result = [parser(x) for x in range(borders[0], borders[1]+1)]
    return result


def to_single_list(large_list):
    result = []
    large_list = list(large_list) if type(large_list) == "<class 'dict_values'>" else large_list
    while isinstance(large_list[0], list):
        for sub in large_list:
            result.extend(sub if isinstance(sub, list) else [sub])
        large_list, result = result.copy(), []
    return large_list


# =====  Aligning  ===== #
def to_center(value, width=0, pattern='', color=''):
    width = default_width if not width else width
    pattern = ' ' if not pattern else pattern
    length = (width - len(value))
    tab = pattern*(length//2)
    return color + tab + pattern*(length % 2 == 1) + value + tab + font.end


def to_rows(lst, border='', width=0):
    # TODO
    border, width = '' if not border else border, default_width if not width else width
    n = width
    for i, a in enumerate(lst):
        if a.find('\x1b[0m') > -1:
            n += 9
        # elif i == 0:
        #    n += 1
        else:
            n = default_width
        lst[i] = a.ljust(n, ' ') + border
    return lst


# =====    Time    ===== #
def to_time(h, m, s):
    return datetime.time(h, m, s)


def to_hms(s):
    s = to_seconds(s) if isinstance(s, datetime.datetime) else s
    return [s // 3600, s // 60 % 60, s % 60]


def to_seconds(time):
    if isinstance(time, str):
        cur = datetime.datetime.strptime(time, '%H:%M:%S')
    elif isinstance(time, list):
        cur = to_time(time[0], time[1], time[2])
    elif isinstance(time, datetime.datetime):
        cur = time
    else:       # condition
        cur = time
    return int(cur.hour) * 3600 + int(cur.minute) * 60 + int(cur.second)


if __name__ == '__main__':
    print(to_graphic_path(path=sample.main_path))
    print(to_divided(content="Some text is there. Must be. The main thing is believe", offset=2, pattern='.'))
    print(to_interval(gap="1-5", parser=int))
    print(to_interval(gap="5-1", parser=str))
    print(to_single_list(large_list=[[[1, 2, 3], [4, 5, 6]], [7, 8, 9]]))
    print(to_center(value="SomeTitle", width=20, pattern='X', color=font.beige))
    print(to_time(h=18, m=46, s=13))
    print(to_hms(s=datetime.datetime.now()))
    print(to_seconds(time="18:47:20"))

