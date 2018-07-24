import datetime

from FIOS.cfg import Settings as _Settings

default_width = _Settings.width


# =====   Common   ===== #
def to_graphic_path(path):
    """ Change path appearance """
    return path.replace('\\', ' ⟩⟩ ')


def to_divided(content, offset=1, pattern="="):
    """ Put {content} between two dividers with specified offset """
    return pattern * default_width + '\n' * offset + content + '\n' * offset + pattern * default_width


def to_interval(gap, parser=lambda x: type(x)):
    """ Convert string "i-j" format to sorted range """
    # current: i-j -> [i, i+1, ... , j-1, j]
    # update to a-z, A-Z
    borders = list(map(int, gap.split('-')))
    borders.sort()
    return [parser(x) for x in range(borders[0], borders[1]+1)]


def to_single_list(large_list):
    """ Convert N-dimension list to one-dimension list """
    result = []
    large_list = list(large_list) if type(large_list) == "<class 'dict_values'>" else large_list
    for i in range(len(large_list)):
        while isinstance(large_list[i], list):
            for sub in large_list:
                result.extend(sub if isinstance(sub, list) else [sub])
            large_list, result = result.copy(), []
    return large_list


def _rld(string, digit, inc=1):
    """ Replace last digit in file/folder name for successful move """
    string = string.split(str(digit))
    return str(digit).join(string[:-1]) + str(digit + inc) + string[-1]


# =====  Aligning  ===== # TODO: old for delete
def to_center(value, width=default_width, pat='', color=''):
    """ Align value with center """
    return color + ("{:%s^%s}" % (pat, width)).format(value) + '\33[0m'


def to_column(row, border='', width=default_width, color=''):
    """ Align row with column """
    return color + ("{:<%s}" % width).format(row) + border + '\33[0m'


# =====    Time    ===== #
def to_time(h, m, s):
    """ Convert (h, m, s) format to datetime type """
    return datetime.time(h, m, s)


def to_hms(s):
    """ Convert to (h, m, s) format """
    s = to_seconds(s) if isinstance(s, datetime.datetime) else s
    return [s // 3600, s // 60 % 60, s % 60]


def to_seconds(time):
    """ Convert any time type to seconds """
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
    print(to_graphic_path(path=r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS"))
    print(to_divided(content="Some text is there. Must be. The main thing is believe", offset=2, pattern='.'))
    print(to_interval(gap="1-5", parser=int))
    print(to_interval(gap="5-1", parser=str))
    print(to_single_list(large_list=[[[1, 2, 3], [4, 5, 6]], [7, 8, 9]]))
    print(to_single_list(large_list=[1, 23, [5, 6, 7], 16]))
    print(to_center(value="SomeItem", width=20, pat='X', color='\33[36m'))
    print(to_time(h=18, m=46, s=13))
    print(to_hms(s=datetime.datetime.now()))
    print(to_seconds(time="18:47:20"))
    print()
    [print(to_column(x, '|', 30)) for x in ["292 521", "1: 123 312 321", "0: 123 51 2", "2: 123 242 424 123 123", "1: 123 323"]]
    print(_rld(r"F:\Work\CODE\Projects\SortManager\toSort\desktop_2\leather_002_bitmap_2.sbsar", 2))
    print(_rld(r"leather_002_bitmap_2.sbsar", 2))