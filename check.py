import os
import os.path as op
import re

from FIOS.sample import engchars as _eng
from FIOS.substance import init as _init
from FIOS.convert import _rld
from FIOS.split import file as sp_file


# TODO
def time():
    pass


# TODO
def mistake():
    pass


# TODO
def intersection():
    pass


def duplicate(source, destination):
    src = _init(source)
    if op.exists(op.join(destination, src.name)):   # TODO: check (1)(2) ...; folders merger or inc index by input
        old, ext = sp_file(src.name)
        ext, res = ext if not ext else '.' + ext, re.findall("\d+", old)
        if res and str(old[-1:]).isdigit():
            digit = int(res[-1]) + 1
            new = _rld(old, digit - 1)
        else:
            digit = 1
            new = old + "_%d" % digit
        while op.exists(op.join(destination, new + ext)):
            new = _rld(new, digit)
            digit += 1
        return op.join(src.dir, new + ext)
    else:
        return False


def name(full_path):
    path, fullname = os.path.split(full_path)
    os.chdir(path)
    lst = fullname.split('.')
    if len(lst) > 2:
        newname = ''
        for i in range(0, len(lst) - 1):
            newname += lst[i]
        newname += '.' + (str(lst[len(lst) - 1])).lower()
        if os.path.exists(os.path.join(path, fullname)):
            os.rename(fullname, newname)
        fullname = newname
    return fullname


def digits(digit_list, pow_=1):
    try:
        if not isinstance(digit_list, (list, str)):
            digit_list = [digit_list]
        for j, i in enumerate(digit_list):
            if i.isdigit():
                i = int(i)
                if i < 10**(pow_-1):
                    digit_list[j] = (pow_ - len(str(i)))*'0' + str(i)
    except():
        pass
    return digit_list


def verb(word, parent='get'):   # TODO:
    # inspect
    v = [False, False, False]
    exc = 'bpdtnml'
    lastchar = word[::-1].lower() if len(word) <= 3 else word[len(word):len(word) - 4:-1].lower()
    # correct verb
    for i in _eng['vowels']:
        if lastchar[0] == i and i != 'y':
            word = word[0:len(word) - 1:] + 'ing'
            v[2] = True
        elif lastchar[1] == i:
            v[0] = True
        if lastchar[2] == i:
            v[1] = True
    else:
        for i in exc:
            if lastchar[0] == i and not (v[0] and v[1]) and lastchar[1] != 'r':
                word += i + 'ing'
                break
        else:
            if not v[2]:
                word += 'ing'
    return word


'''def dircontent(path):
    files, dirs = list(get.subs(path, False, True))[0], list(sample.dirs.keys())
    count = [0]*len(dirs)
    if len(files) == 0:
        return (font.grey + 'empty' + font.end), [0]
    elif len(files) < 3100:
        for f in files:
            name = init(f).name
            for filedir in (sample.files.values()):
                if get.exceptions(name, filedir, mode='ext'):
                    count[dirs.index(filedir[0])] += 1
        count, dirs = (list(t) for t in zip(*sorted(zip(count, dirs), reverse=True)))
    dirs, count = list(dirs[0:5:]), list(count[0:5:])
    return dirs, count'''

if __name__ == "__main__":
    print(digits(['1', '0002', '3', 'abs', 12.3, '04', '25', '23', '04', '107'], 2))
