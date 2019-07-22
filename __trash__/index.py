import os
import codecs

import FIOS.font as _font
from FIOS.substance import init as _init
from FIOS.write import to_file as _to_file
from FIOS.read import from_file as _from_file
from FIOS.notifier import message_console as _mc, result as _r

dir_tmp = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp"
used_tmp, exc_tmp = "used_branches.txt", "exc_branches.txt"
default_used = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\used_branches.txt"
default_exc = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\exc_branches.txt"
_fl = 2


# =====    Extra   ===== #
def string(value, color=_font.red2):
    """ Index string by color """
    return color + value + _font.end


def content(value, pattern):
    """ Search and Index <pattern> in <value> and return indexes """
    res = []
    for i in range(len(str(value))):
        if str(value)[i] == pattern:
            res.append(i)
    return res if len(res) > 0 else -1


# =====   General   ===== #
def new(full_path, public=False, fl=_fl):
    """ Create new index_file by <full_path> """
    def create(path, _content="", _public=False):
        item = _init(path, fl=fl)
        success = False
        if item.kind == "path" and not item.exist:
            if item.type in ["folder", "ambiguous"]:
                try:
                    os.makedirs(path)
                    success = True
                except Exception as _e:
                    print(_font.paint(_e, _font.red))
            elif item.type == "file":
                if not os.path.exists(item.dir):
                    create(item.dir)
                with codecs.open(path, "w", "utf-8") as my_file:
                    my_file.write(_content)
                success = True
            else:
                success = None
        _r(path, success, "create") if _public else None
        return success

    try:
        create(full_path, _public=public)
    except Exception as e:
        print(e)


def append(index_file, *args, public=False, fl=_fl):
    """ Append <*args> into index_file by <data_path> """
    args = args[0] if isinstance(args[0], list) else args
    if not os.path.exists(index_file):
        new(index_file, public)

    wroten = get(index_file, fl=fl)
    s_args = [x for x in args if x not in wroten]
    if s_args:
        success = _to_file(index_file, '\r\n'.join(s_args) + '\r\n', 'a')
    else:
        success = None
    [_r(x, success, "index") for x in args] if public else None


def get(index_file, mode="indexed", public=False, fl=_fl):
    """ Get indexed items from <data_path> """
    data_links = False, []
    try:
        _data = _init(index_file, fl=fl)
        os.chdir(_data.dir)
        data_links = _from_file(index_file).split('\r\n')[:-1:]
    except Exception as e:
        print(e)
    _mc(os.path.split(index_file)[1], "reading...") if public else None
    for link in data_links:
        _mc(link, 'was %s.' % mode, _init(link, fl=fl).sign, _font.grey) if public else None
    return data_links


def clean(index_file, public=False, fl=_fl):
    """ Clean <data_path> with indexed items """
    success = False
    try:
        _data = _init(index_file, fl=fl)
        os.chdir(_data.dir)
        _to_file(index_file, '')
        success = True
    except Exception as e:
        print(e)
    _r(index_file, success, "clean") if public else None


def files(out_list, check_list, indexed_list, color=_font.grey):
    """ Index items from <check_list> by <indexed_list> and return it in <out_list> with <color>"""
    index_list, special = [], []
    if check_list:
        if not isinstance(check_list[0], str):
            check_list = [x.content for x in check_list]

    for indexed_path in indexed_list:
        if indexed_path in check_list:
            index_list.append(list(check_list).index(indexed_path))
            special.append(indexed_path)
    return [_font.paint(x, color, total=True) if i in index_list else x for i, x in enumerate(out_list)], special


if __name__ == "__main__":
    data = [r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\used_branches.txt",
            r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\exc_branches.txt"]

    print(string(value="SomeString. Mark me. pleeease ^___^", color=_font.beige))
    print(content(value="Hello. It's Me", pattern="'"))
    print(content(value=type("Hello. It's Me"), pattern="'"))

    def test_cycle():
        # new(os.getcwd(), True)

        for j in range(2):
            append(data[j], ["1", "2", "3"], public=True)
            data_list = get(data[j], public=True) if j == 0 else get(data[j], "blocked", True)
            clean(data[j], True)

    # clean(data[0], public=True)
    # append(data[0], [r"F:\Work\CODE\Projects\SortManager\toSort\HelloWorld",
    #       r"F:\Work\CODE\Projects\SortManager\toSort\vk"], public=True)
    path = r"F:\Work\CODE\toStudy\Python\.idea"
    append(default_exc, path, public=True)
