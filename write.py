from datetime import datetime
import os
import codecs

import FIOS.font as font
import FIOS.convert as convert
import FIOS.sample as sample

width = sample.width
# =====   Common   ===== #


def me(value, start='', end='', name='', access=True):
    if access:
        if isinstance(value, list):
            if name:
                print(font.beige + name + font.end + ' reference:')
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
            lst = list(map(lambda k, v: "{}[{}]{} - ".format(font.beige, k, font.end) + str(v), keys, values))
            me(lst, name=name)
        elif isinstance(value, str):
            print(value)


def list_(array, arrayname='List', colormode='iri'):
    # color = {'iri': font.end, 'temp':}
    lstname = arrayname.capitalize() + ':'
    lst = array
    if colormode == 'iri':
        print(font.beige + lstname + font.end)
        for i, f in enumerate(lst):
            print(font.beige + '%s. ' % (str(int(i) + 1)) + font.end + f + font.end)
    elif colormode == 'temp':
        print(font.underline + lstname + font.end)
        for i, f in enumerate(lst):
            print('%s. ' % (str(int(i) + 1)) + font.violet + f + font.end)
    elif colormode == 'navigator':
        print(lstname)
        for i, f in enumerate(lst):
            if i == 0:
                f = '▲ toParent'
            print(font.yellow + '%s. ' % (str(int(i))) + font.end + f + font.end)
# =====  Built-in  ===== #


def priority(mainlist, sidelist='', public=True, colorize=True):
    sidelist, string = ([''] * len(mainlist) if not sidelist else sidelist), ''

    for m, s, color in zip(mainlist, sidelist, sample.priority):
        if s:
            color = '' if not colorize else color
            string += ('{2}{0}({1}) '.format(m, s, color))

    string = string + font.end if colorize else string
    me(string, access=public)
    return string
# =====    Time    ===== #


def hms(time='', end=''):
    time = [datetime.now().hour, datetime.now().minute, datetime.now().second] if not time else time
    hour, minute, second = time
    conv = convert.to_datetime(hour, minute, second)
    conv = conv.strftime('%H:%M:%S')
    end = '\n' if not end else end
    print(font.beige2 + conv + font.end, end=end)
# =====    File    ===== #


def to_file(filepath, content, mode='w'):
    dir_, name = os.path.split(filepath)
    os.chdir(dir_)
    with codecs.open(name, mode, 'utf-8') as output:
        output.write(content)
