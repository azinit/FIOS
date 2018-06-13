from datetime import datetime

import font

# =====   Common   ===== #


def to_graphic_path(path):
    path = path.replace('\\', ' ⟩⟩ ')
    return path


def from_gap(string, str_=True):
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


def to_center(value, width=39, pattern='', color=''):
    # width = Feebon.LINE if not width else width
    pattern = ' ' if not pattern else pattern
    color = font.beige if not color else color
    tab = str(value.rjust(width, pattern)).replace(value, '', 1)
    tab2 = tab[:len(tab)//2:]
    tab1 = tab2 if len(value) % 2 == 0 else tab2 + pattern
    value = color + tab1 + value + tab2 + font.end
    return value


def to_rows(lst, border='', width=''):
    width = 57 if not width else width
    n = width
    for i, a in enumerate(lst):
        if a.find('\x1b[0m') > -1:
            n += 9
        elif i == 0:
            n += 1
        else:
            n = width
        lst[i] = a.ljust(n, ' ') + border
    return lst
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
