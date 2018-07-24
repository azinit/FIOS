import os

from FIOS.font import yellow as _yellow, blue as _blue, end as _end, beige as _beige
from FIOS.sample import MAIN_PATH as _MP, files as _files
from FIOS.convert import to_seconds as _to_s, to_hms as _to_hms, to_single_list as _to_sng
from FIOS.substance import init as _init
from FIOS.notifier import status as _s


# =====   Common   ===== #)
# TODO : function: path_intersection(deeepest up lvl)
def intersection():
    pass


def digit(digit_seq):
    count_list = [0] * 10
    for e in digit_seq:
        if str(e).isdigit():
            count_list[int(e)] += 1
    return count_list


def key_by_value(search, dictionary):
    for key, value in dict(dictionary).items():
        value = [value] if not isinstance(value, list) else _to_sng(value)
        if search in value:
            return key


# =====  File Sys  ===== #
def subs(path, folders=True, files=False, public=False, recursive=True):
    def unite(main_dir, sub_list):
        return list(map(lambda x: os.path.join(main_dir, x), sub_list))

    _s(pattern='.', color=_beige) if public else None
    dst, level = _init(path), 0
    root = os.path.split(dst.content)[0] if dst.kind == 'file' else dst.content
    if root:
        result_files, result_folders = [], [root] if folders else []
        for rootName, folderNames, fileNames in os.walk(root):
            if not recursive and level > 0:
                break
            if folders and recursive:
                result_folders.extend(unite(rootName, folderNames))
            if files:
                result_files.extend(unite(rootName, fileNames))
            level += 1
        if public:
            [print(_yellow, _init(x).sign, x, _end) for x in result_folders]
            [print(_blue, _init(x).sign, x, _end) for x in result_files]
        if files and folders:
            return result_folders, result_files
        elif files:
            return [], result_files
        elif folders:
            return result_folders, []
        else:
            return [], []


# =====    Time    ===== #
def time(start_time, end_time):
    if not isinstance(start_time, int):
        start_time, end_time = _to_s(start_time), _to_s(end_time)
    i, j = min(start_time, end_time), max(start_time, end_time)
    for i in range(i, j+1):
        yield _to_hms(i)


if __name__ == "__main__":
    print(intersection())
    print(digit(digit_seq="12349501"))
    print(key_by_value(search=".avi", dictionary=_files))
    subs(path=_MP, folders=True, files=True, public=True, recursive=False)
    print(list(time(start_time=64800, end_time=64809)))
