import os

import FIOS.substance as substance
import FIOS.font as font
import FIOS.sample as sample
import FIOS.write as write
import FIOS.notifier as notifier
import FIOS.convert as convert

# =====   Common   ===== #)


# TODO
def intersection():
    pass


def substring(string, pattern):
    res = [x for i, x in enumerate(str(string).split(pattern)) if i % 2 == 1]
    return res[0] if len(res) == 1 else res


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

    notifier.status() if public else None
    dst, level = substance.initialize(path), 0
    root = os.path.split(dst.content)[0] if dst.kind == 'file' else dst.content
    if root:
        result_files, result_folders = [], [root] if folders else []
        for dirName, folderNames, fileNames in os.walk(root):
            if not recursive and level > 0:
                break
            if folders and recursive:
                result_folders.extend(unite(dirName, folderNames))
            if files:
                result_files.extend(unite(dirName, fileNames))
            level += 1
        if public:
            write.me(result_folders, font.yellow + sample.objects['folder'], font.end)
            write.me(result_files, font.blue + sample.objects['file'], font.end)
        if files:
            yield result_files
        if folders:
            yield result_folders
# =====    Time    ===== #


def time(start_time, end_time):
    if not isinstance(start_time, int):
        start_time, end_time = convert.to_seconds(start_time), convert.to_seconds(end_time)
    i, j = min(start_time, end_time), max(start_time, end_time)
    for i in range(i, j+1):
        yield convert.to_hms(i)


if __name__ == "__main__":
    print(intersection())
    print(substring(string=type("SomeString"), pattern="'"))
    print(digit(digit_seq="12349501"))
    print(key_by_value(search=".avi", dictionary=sample.files))
    folder, file = subs(path=sample.main_path, folders=True, files=True, public=True, recursive=False)
    print(list(time(start_time=64800, end_time=64809)))
