def def_file(self):
    file = get.obj(self).content
    if not file:
        us = USED_PATH
    else:
        us = file
    return us

def new(self = MPATH, file =''):
    path = get.obj(self).path
    us = marker.def_file(file)
    # ==========================
    createf('temp', path)
    spath = os.path.join(path, 'temp')
    shutil.copy('name.txt', spath)
    os.chdir(spath)
    name = 'usedbase' + '.txt'
    os.rename('name.txt', name)
    print(font.yellow + name + font.end + ' created!')

def append(self = MPATH, file =''):
    path = get.obj(self).path
    us = marker.def_file(file)
    # ==========================
    os.chdir(os.path.join(MPATH, 'temp'))
    with codecs.open(us, 'a', 'utf-8') as usedbase:
        usedbase.writelines(path)
        usedbase.writelines('\n')
        # print(font.grey + path + font.end + ' added as used!')
def check(self = MPATH, file =''):
    path = get.obj(self).path
    us = marker.def_file(file)
    # ==========================
    used = []
    os.chdir(os.path.join(MPATH, 'temp'))
    with codecs.open(us, 'r+', 'utf-8') as usedbase:
        for lines in usedbase:
            lines = lines[:-1:]
            used.append(lines)
    # for u in used:
    #    print(font.ext.grey + u + font.ext.end + ' was used!')
    return used
def clean(self = MPATH, file =''):
    path = get.obj(self).path
    us = marker.def_file(file)
    # ==========================
    os.chdir(os.path.join(MPATH, 'temp'))
    with codecs.open('usedbase.txt', 'w', 'utf-8') as usedbase:
        usedbase.write('')
        print(font.red + 'usedbase.txt' + font.end + ' cleaned!')

def content(self, pattern):
    content = get.obj(self).content
    if isinstance(content, str):
        i = content.find(pattern)
        return i
    else:
        return None

def string(line, color = 'std'):
    string = get.obj(line).string
    if color == 'std':
        string = font.red + string + font.end
    elif color == 'iri':
        string = font.beige2 + string + font.end
    return string