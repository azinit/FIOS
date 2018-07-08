import os

import FIOS.init as init
import FIOS.font as font
import FIOS.sample as sample
import FIOS.write as write
import FIOS.notifier as notifier
import FIOS.convert as convert

# =====   Common   ===== #


def info(value, name=''):
    obj = init.obj(value, 'none') if name == '' else init.obj(value, name)
    notifier.status()
    print('%s name: %s' % (obj.kind, font.beige + obj.name + font.end))
    print('%s type: %s' % (obj.kind, font.beige + obj.type + font.end))
    print('%s %s: %s' % (obj.kind, obj.ps, font.beige + str(obj.content) + font.end))


def intersection(value, comparewith):
    # f: string intersection
    if value and comparewith:
        result = []
        if not isinstance(value, list) and isinstance(comparewith, list):
            if isinstance(comparewith[0], list):
                for sublist in comparewith:
                    b = intersection(value, sublist)
                    if b:
                        result.append(b)
                        break
            else:
                result = False if comparewith.count(value) < 1 else value
                return result
        elif isinstance(value, list) and isinstance(comparewith, list):
            for subvalue in value:
                if isinstance(subvalue, list):
                    for subsubvalue in subvalue:
                        b = (intersection(subsubvalue, comparewith))
                        if b:
                            result.append(b)
                else:
                    b = (intersection(subvalue, comparewith))
                    if b:
                        result.append(b)

        return convert.to_single_list(result)


def digit(value, digits=''):
    digits, exclist = [0] * 10 if not digits else digits, list(range(0, 10))
    for e in value:
        if str(e).isdigit():
            digits[int(e)] += 1
    return digits


def key_(value_search, dictionary):
    for subkey, value in dictionary.items():
        if isinstance(value, list):
            for subvalue in value:
                if subvalue == value_search:
                    return subkey
        else:
            if value == value_search:
                return subkey
# =====  File Sys  ===== #


def subs(path, fld=True, fls=False, public=False, recursive=True):
    if public:
        notifier.status()
    dst, level = init.obj(path), 0
    root = os.path.split(dst.path)[0] if dst.kind == 'File' else dst.path
    if root:
        dirs = [root] if fld else []
        files = []
        for dirName, dirNames, fileNames in os.walk(root):
            if not recursive and level > 0:
                break
            if fld and recursive:
                dirs.extend(list(map(lambda subname: os.path.join(dirName, subname), dirNames)))
            if fls:
                files.extend(list(map(lambda filename: os.path.join(dirName, filename), fileNames)))
            level += 1
        if public:
            write.me(dirs, font.yellow + sample.objtype['folder'], font.end)
            write.me(files, font.blue + sample.objtype['file'], font.end)
        if fls:
            yield files
        if fld:
            yield dirs
# =====    Time    ===== #


def time(startime, endtime):
    cur, end = convert.to_seconds(startime), convert.to_seconds(endtime)
    i, j = min(cur, end), max(cur, end)
    for i in range(i, j+1):
        yield convert.to_hms(i)

if __name__ == "__main__":
    # info([1, 1, 2, 3, 5])
    # info("It's string")
    # files, dirs = subs("F:\Database\Sort", True, True, True, True)
    # print(key_(".zpr", sample.files))
    # s = list(time("13:41:00", "14:01:13"))
    print(intersection([1], ['1',1,2,1]))
