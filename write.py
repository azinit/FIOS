import os
import codecs
from datetime import datetime as d

from FIOS.font import beige2 as _beige2, end as _end
from FIOS.convert import to_time as _to_time
from FIOS.notifier import result as _r, status as _s


# =====   Common   ===== #
# TODO: remove old
'''def me(value, start='', end='', name='', access=True): 
    if access:
        if isinstance(value, list):
            if name:
                print(font.red2 + name + font.end + ' reference:')
            if len(value) > 0:
                if isinstance(value[0], list):
                    for line in value:
                        print(line)
                else:
                    if start:
                        value = '\n'.join(list(map(lambda x: start + ' ' + str(x) + ' ' + end, value)))
                    else:
                        value = '\n'.join(list(map(str, value)))
                    print(value)
        elif isinstance(value, dict):
            keys, values = value.keys(), value.values()
            lst = list(map(lambda k, v: "{}[{}]{} - ".format(font.red2, k, font.end) + str(v), keys, values))
            me(lst, name=name)
        elif isinstance(value, str):
            print(value)'''


'''def list_(array, arrayname='List', colormode='iri'):
    # color = {'iri': font.end, 'temp':}
    lstname = arrayname.capitalize() + ':'
    lst = array
    if colormode == 'iri':
        print(font.red2 + lstname + font.end)
        for i, f in enumerate(lst):
            print(font.red2 + '%s. ' % (str(int(i) + 1)) + font.end + f + font.end)
    elif colormode == 'temp':
        print(font.underline + lstname + font.end)
        for i, f in enumerate(lst):
            print('%s. ' % (str(int(i) + 1)) + font.violet + f + font.end)
    elif colormode == 'navigator':
        print(lstname)
        for i, f in enumerate(lst):
            if i == 0:
                f = '▲ toParent'
            print(font.yellow + '%s. ' % (str(int(i))) + font.end + f + font.end)'''


# =====  Built-in  ===== #
'''def priority(mainlist, sidelist='', public=True, colorize=True):
    sidelist, string = ([''] * len(mainlist) if not sidelist else sidelist), ''

    for m, s, color in zip(mainlist, sidelist, sample.priority):
        if s:
            color = '' if not colorize else color
            string += ('{2}{0}({1}) '.format(m, s, color))

    string = string + font.end if colorize else string
    me(string, access=public)
    return string'''


# =====    Time    ===== #
def hms(time='', end=''):
    time = [d.now().hour, d.now().minute, d.now().second] if not time else time
    hour, minute, second = time
    converted = _to_time(hour, minute, second)
    converted = converted.strftime('%H:%M:%S')
    end = '\n' if not end else end
    print(_beige2 + converted + _end, end=end)


# =====    File    ===== #
# TODO: add binary mod for media
def to_file(file_path, content, mode='w', public=False):
    """ Write something to file by path """
    path, name = os.path.split(file_path)
    success = False
    if public:
        _s()
        _r(path, os.path.exists(path), "cur_dir")
        _r(file_path, os.path.exists(file_path), "write", decore=lambda x: os.path.split(x)[1])

    if os.path.exists(file_path):
        os.chdir(path)
        with codecs.open(name, mode, "utf-8") as output:
            output.write(content)
            success = True

    return success
