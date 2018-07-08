from datetime import datetime

import font
import cfg

sections = ['Common', 'Aligning', 'Time']
functions = [['to_graphic_path', 'from_gap', 'to_simple_list'], ['to_center', 'to_rows'], ['to_datetime', 'to_hms', 'to_seconds']]
width = int(cfg.get(cfg.iCore, 'General', 'line_amount'))  # from cfg
version = 2.0
# =====   Common   ===== #


def to_graphic_path(path):
    path = path.replace('\\', ' ⟩⟩ ')
    return path


def from_gap(string, str_=True):
    # current: i-j -> [i, i+1, ... , j-1, j]
    # update to a-z, A-Z
    gap, result = list(map(int, string.split('-'))), []
    gap.sort()
    for i in range(gap[0], gap[1] + 1):
        result.append(i)
    result = list(map(int, result)) if str_ else result
    return result


def to_simple_list(largelist):
    result = []
    while isinstance(largelist[0], list):
        for sub in largelist:
            result.extend(sub)
        largelist, result = result.copy(), []
    return largelist
# =====  Aligning  ===== #


def to_center(value, w=0, pattern='', color=''):
    w, pattern, color = width if not w else w, ' ' if not pattern else pattern, font.beige if not color else color
    leng = (w - len(value))
    tab = pattern*(leng//2)
    value = color + tab + pattern*(leng % 2 == 1) + value + tab + font.end
    return value


def to_rows(lst, border='', w=0):
    # need to upd
    border, w = '' if not border else border, width if not w else w
    n = w
    for i, a in enumerate(lst):
        if a.find('\x1b[0m') > -1:
            n += 9
        # elif i == 0:
        #    n += 1
        else:
            n = width
        lst[i] = a.ljust(n, ' ') + border
    return lst


def with_shell(value, w=0, pattern=''):
    w, pattern = width if not w else w, ' ' if not pattern else pattern
    res = pattern*w + '\n' + value + '\n' + pattern*w
    return res
# =====    Time    ===== #


def to_datetime(h, m, s, dy=13, mn=12, yr=2013):
    return datetime(yr, mn, dy, h, m, s)


def to_hms(s):
    s = to_seconds(s) if isinstance(s, datetime) else s
    return [s // 3600, s // 60 % 60, s % 60]


def to_seconds(time):
    if isinstance(time, str):
        cur = datetime.strptime(time, '%H:%M:%S')
    elif isinstance(time, list):
        cur = to_datetime(time[0], time[1], time[2])
    elif isinstance(time, datetime):
        cur = time
    else:       # condition
        cur = time
    return int(cur.hour) * 3600 + int(cur.minute) * 60 + int(cur.second)


if __name__ == '__main__':
    # print(from_gap('1-3'))

    # array = [[x for x in range(13)], [x**2 for x in range(10) if x % 2 == 0], [x/2 for x in range(100) if x % 13 == 0]]
    # print(array)
    # print(to_simple_list(array))

    # print(to_center('Iri', pattern='=', color=font.blink))
    pass
