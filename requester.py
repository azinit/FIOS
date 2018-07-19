import re

import FIOS.sample as sample

requests_help = {
    # general
    "help": "Get help on requests",
    "undo": "Cancel last operation",
    "exit": "Finish program",
    # tags
    "-ch": "Choose",                    # > -ch step
    "-rec": "Start recursive action",   # > -rec (sort)
    "-s -type": "Sort by filetype",
    "-g": "Get something",              # > -g folders/files
    "-i": "Index some object",          # > -i exception
    # explorer actions
    "ref": "Refresh Directory Content",
    "open": "Open Current Directory",
    "move {src} {dst}": "Move {source} to {destination}",
    "type i": "Get type of {i} folder",
    "del i": "Delete {i}",
    "clean": "Clean {cur_dir}from empty dirs",
    # "-i exception": "Set Extension Directory",
    # "-ch step": "choose step",
    # "-g folders": "Get Subs of Current Directory",
    # "-g files": "Get Files of Current Directory",
}

requests = {
    # general
    "help": "Get help on requests",
    "undo": "Cancel last operation",
    "exit": "Finish program",
    # tags
    "-ch": "Choose",                    # > -ch step
    "-rec": "Start recursive action",   # > -rec (sort)
    "-s type": "Sort by filetype",
    "-g": "Get something",              # > -g folders/files
    "-i": "Index some object",          # > -i exception
    # explorer actions
    "ref": None,
    "open": "Open Current Directory",
    "move {src} {dst}": "Move {source} to {destination}",
    "type i": "Get type of {i} folder",
    "del i": "Delete {i}",
    "clean": "Clean {cur_dir}from empty dirs",
    # "-i exception": "Set Extension Directory",
    # "-ch step": "choose step",
    # "-g folders": "Get Subs of Current Directory",
    # "-g files": "Get Files of Current Directory",
}


# [False, True, None] == [Exit, GoNext, Refresh]
def console(user_input):
    if user_input == "":
        return False
    else:
        return True


def start(*args):
    print(args[1:]) if len(args) > 1 else None
    print(str(args[0]).capitalize(), sample.choicebox[0], '?: ')
    user_input = input('> ')

    if user_input in ['', 'y']:
        return True
    else:
        return False


if __name__ == "__main__":
    result = console("-ch step")
    print(result)
