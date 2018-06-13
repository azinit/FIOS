import os

# import write
# import font
# import sample
# import get



# TODO
def time(value):
    pass


# TODO
def mistake(self):
    pass


# TODO
def intersection(arg1, arg2=''):
    if arg2:
        intersection, source, destination = [], arg1, arg2
        for a in source:
            for b in destination:
                if b.find(a) != -1:
                    intersection.append(a)
        return intersection
    else:
        spath, cur = arg1, []
        for f in spath:
            if os.path.isdir(f):
                list1, list2 = (check.dircontent(f))
                cont = write.priority(list1, list2, False, False).split('(')
                for i, c in enumerate(cont):
                    if c:
                        b = ''.join(re.findall('[A-Za-z]', c))
                        if b:
                            cont[i] = b
                        else:
                            cont.pop(i)
                if len(cont) > 3 and len(spath) == 1:
                    cur = cont
                    break
                if not cur:
                    cur = cont
                else:
                    bol = check.intersection(cur, cont)
                    if bol:
                        cur = bol
                    else:
                        cur.clear()
                        break
            else:
                Type = ''
                for file in sample.files.values():
                    if (get.exceptions(f, file, mode='ext')[0]):
                        Type = file[0]
                        break
                if not cur:
                    cur.append(Type)
                elif cur[0] != 'Type':
                    cur.clear()
                    return cur

        return cur


def duplicate(filepath, fullname):
    dst = os.path.split(filepath.path)[0]
    b = False
    while not b:
        path = dst + '/' + fullname
        if os.path.exists(path):
            new, ext = fullname.split('.')
            try:
                new, brk = new.split('(')
                brk = brk[0:len(brk) - 1:]
                if int(brk):
                    brk = '(' + str(int(brk) + 1) + ')'
                os.rename(fullname, new + brk + '.' + ext)
                fullname = new + brk + '.' + ext
            except:
                os.rename(fullname, new + '(2).' + ext)
                fullname = new + '(2).' + ext
        else:
            b = True
    return fullname


def name(commonpath):
    path, fullname = os.path.split(commonpath)
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


def digits(diglist):
    b = False
    try:
        if not isinstance(diglist, list) and not isinstance(diglist, str):
            diglist = [diglist]
            b = True
        for j, i in enumerate(diglist):
            if int(i) < 10:
                diglist[j] = '0' + str(i)
        if b:
            return diglist[0]
        else:
            return diglist
    except:
        return diglist


def verb(word, parent='get'):
    # inspect
    v = [False, False, False]
    exc = 'bpdtnml'
    lastchar = word[::-1].lower() if len(word) <= 3 else word[len(word):len(word) - 4:-1].lower()
    # correct verb
    for i in sample.engchars.get('vowels'):
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


def input(message):
    b = True if message == 'y' or message == '' else False
    return b


def dircontent(path):
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
    return dirs, count
