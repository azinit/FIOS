import inspect

import FIOS.font as font
import FIOS.convert as convert
import FIOS.sample as sample

width = sample.width


def result(obj, b, mode):
    # TODO
    # None event
    sign, col = '13F', [font.red2] + [font.blue2] + [font.end]
    mdd = {
        'create': ['13F already exists!', 'Created: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'clean': ['Cleaning 13F failed.', 'Cleaned: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'sort': ['Sorting the 13F failed.', 'Sorted: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'move': ['empty', 'empty', 'empty'],
        'read': ['File 13F not found', 'Reading: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'curdir': ['13F not found', 'Directory: 13F', '{}Error{} occurred'.format(font.yellow, font.end)]
    }
    print(mdd[mode][2] if b is None else mdd[mode][b].replace(sign, str(col[b] + obj + col[2])))


def status(tag='', pattern='', w=0):
    name = str(inspect.stack()[1][3]) if not tag else tag
    pattern = '-' if not pattern else pattern
    w = width if not w else w
    name = convert.to_center(name.upper(), w, pattern)
    print(name)
