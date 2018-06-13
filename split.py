import os


def file(filename):
    result = filename.split('.')
    if len(result) == 1:
        fnm = result[0]
        fext = ''
    elif len(result) == 2:
        fnm = result[0]
        fext = result[1]
    elif len(result) > 2:
        fnm = '.'.join(result[:len(result) - 1:])
        fext = result[len(result) - 1]
    else:
        return '0', '0'
    return fnm, fext


def path(path, it=2):
    s, newpath, path = '', [], [path]
    for i in range(0, it):
        path = os.path.split(path[0])
        newpath.insert(0, path[1])
    return r'\\'[1].join(newpath)
