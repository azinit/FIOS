import os
import FIOS.notifier as notifier

substance, smp, convert = notifier.subst, notifier.smp, notifier.convert
yellow, blue, end = smp.font.yellow, smp.font.blue, smp.font.end


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
        value = [value] if not isinstance(value, list) else convert.to_single_list(value)
        if search in value:
            return key


# =====  File Sys  ===== #
def subs(path, folders=True, files=False, public=False, recursive=True):
    def unite(main_dir, sub_list):
        return list(map(lambda x: os.path.join(main_dir, x), sub_list))

    notifier.status(pattern='.', color=smp.font.beige) if public else None
    dst, level = substance.init(path), 0
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
            [print(yellow, substance.init(x).sign, x, end) for x in result_folders]
            [print(blue, substance.init(x).sign, x, end) for x in result_files]
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
        start_time, end_time = convert.to_seconds(start_time), convert.to_seconds(end_time)
    i, j = min(start_time, end_time), max(start_time, end_time)
    for i in range(i, j+1):
        yield convert.to_hms(i)


if __name__ == "__main__":
    print(intersection())
    print(digit(digit_seq="12349501"))
    print(key_by_value(search=".avi", dictionary=smp.files))
    subs(path=smp.MAIN_PATH, folders=True, files=True, public=True, recursive=False)
    print(list(time(start_time=64800, end_time=64809)))
