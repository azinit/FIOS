from datetime import datetime
import os
import codecs
import convert
import inspect


import font
import sample

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


def status(tag='', pattern='', width=39, access=True):
    if access:
        name = str(inspect.stack()[1][3]) if not tag else tag
        pattern = '-' if not pattern else pattern
        # width = Feebon.LINE if not width else width
        name = convert.to_center(name.upper(), width, pattern)
        print(name)


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


def priority(mainlst, sidelst='', printmode=True, colormode=True):
    sidelst, string = (['']*len(mainlst) if not sidelst else sidelst), ''

    for m, s, color in zip(mainlst, sidelst, sample.priority):
        if s:
            color = '' if not colormode else color
            string += ('{2}{0}({1}) '.format(m, s, color))

    string = string + font.end if colormode else string
    me(string, access=printmode)
    return string


def notification(path, b, mode='create', access=True):
    if access:
        sign, col = '13F', [font.red] + [font.blue] + [font.end]
        mdd = {
            'create': ['13F already exists!', 'Created: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
            'clean': [],
            'sort': [],
            'move': [],
            'read': ['13F not found', 'Reading: 13F', '{}Error occured'.format(font.yellow, font.end)],
            'curdir': ['13F not found', 'Directory: 13F', '{}Error occured'.format(font.yellow, font.end)]
        }
        print(mdd[mode][2] if b is None else mdd[mode][b].replace(sign, str(col[b] + path + col[2])))
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





