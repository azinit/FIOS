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


# =====    Extra   ===== #
def string(value, color=_font.red2):
    return color + value + _font.end


def content(value, pattern):
    res = []
    for i in range(len(str(value))):
        if str(value)[i] == pattern:
            res.append(i)
    return res if len(res) > 0 else -1


# =====   General   ===== #
def new(full_path, public=False):
    def create(path, _content="", _public=False):
        item = _init(path)
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


def append(data_path, *args, public=False):
    args = args[0] if isinstance(args[0], list) else args
    if not os.path.exists(data_path):
        new(data_path, public)

    wroten = get(data_path)
    s_args = [x for x in args if x not in wroten]
    if s_args:
        success = _to_file(data_path, '\r\n'.join(s_args) + '\r\n', 'a')
    else:
        success = None
    [_r(x, success, "index") for x in args] if public else None


def get(data_path, mode="used", public=False):
    data_links = False, []
    try:
        _data = _init(data_path)
        os.chdir(_data.dir)
        data_links = _from_file(data_path).split('\r\n')[:-1:]
    except Exception as e:
        print(e)
    _mc(os.path.split(data_path)[1], "reading...") if public else None
    for link in data_links:
        _mc(link, 'was %s.' % mode, _init(link).sign, _font.grey) if public else None
    return data_links


def clean(data_path, public=False):
    success = False
    try:
        _data = _init(data_path)
        os.chdir(_data.dir)
        _to_file(data_path, '')
        success = True
    except Exception as e:
        print(e)
    _r(data_path, success, "clean") if public else None


def files(label_list, check_list, to_index_list, color=_font.grey):
    index_list = []
    for index_path in to_index_list:
        if index_path in check_list:
            index_list.append(list(check_list).index(index_path))
    return [_font.paint(x, color) if i in index_list else x for i, x in enumerate(label_list)]


if __name__ == "__main__":
    data = [r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\used_branches.txt",
            r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\exc_branches.txt"]
    def test_cycle():
        print(string(value="SomeString. Mark me. pleeease ^___^", color=_font.beige))
        print(content(value="Hello. It's Me", pattern="'"))
        print(content(value=type("Hello. It's Me"), pattern="'"))
        # new(os.getcwd(), True)

        for j in range(2):
            append(data[j], ["1", "2", "3"], public=True)
            data_list = get(data[j], public=True) if j == 0 else get(data[j], "blocked", True)
            clean(data[j], True)

    # clean(data[0], public=True)
    # append(data[0], [r"F:\Work\CODE\Projects\SortManager\toSort\HelloWorld",
    #       r"F:\Work\CODE\Projects\SortManager\toSort\vk"], public=True)
    append(default_exc, r"F:\Work\CODE\Projects\SortManager\toSort\HelloWorld", public=True)
