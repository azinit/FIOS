import inspect

import FIOS.font as font
import FIOS.convert as convert
import FIOS.sample as sample

default_width = sample.width


def result(item, state, mode):
    # TODO
    # None event
    sign, col = '13F', [font.red] + [font.blue2] + [font.end]
    mdd = {
        'create': ['13F already exists!', 'Created: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'clean': ['Cleaning 13F failed.', 'Cleaned: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'sort': ['Sorting the 13F failed.', 'Sorted: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'move': ['empty', 'empty', 'empty'],
        'read': ['Input file 13F not found', 'Reading from: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'write': ['Output file 13F not found', 'Writing to: 13F', '{}Error{} occurred'.format(font.yellow, font.end)],
        'cur_dir': ['13F not found', 'Directory: 13F', '{}Error{} occurred'.format(font.yellow, font.end)]
    }
    print(mdd[mode][2] if state is None else mdd[mode][state].replace(sign, str(col[state] + item + col[2])))


def status(tag='', pattern='', width=0):
    name = str(inspect.stack()[1][3]) if not tag else tag
    pattern = '-' if not pattern else pattern
    width = default_width if not width else width
    name = convert.to_center(name.upper(), width, pattern)
    print(name)


def process():
    pass

def match():
    # TODO
    # right_answer == user_answer ?
    # return red/ blue (user_answer)
    pass

if __name__ == "__main__":
    for i_mode in ["create", "clean", "sort", "move", "read", "write", "cur_dir"]:
        for i_state in [False, True, None]:
            print("{}_{}: ".format(i_mode, i_state), end=' ')
            result(item="SomeItem", state=i_state, mode=i_mode)
    status(tag="SOME-TITLE", pattern='-', width=20)
