import time as _t

from FIOS.font import grey as _grey, end as _end, beige as _beige
from FIOS.sample import choicebox as _box
from FIOS.convert import to_interval as _to_i, to_single_list as _to_s

# TODO: simplify ; rename() ; incorrect words ; match with fm; multiple tags
help_req = {
    "GENERAL":        '',                                # ------
    "undo":           "Cancel last operation",           # X
    "exit":           "Finish program",                  # >
    "":               "Enter",                           # V
    ".TAGS..":        '',                                # ------
    "++":             "Inc",                             # >
    "--":             "Dec",                             # >
    "-r":             "Recursive",                       # V
    "-o":             "Odd",                             # >
    "exc":            "$EXCEPTION",                      # V
    "usd":            "$USED",                           # V
    "-d":             "Dir",                             # >
    "-f":             "File",                            # >
    "-t":             "Type",                            # X
    "EXPLORE":        '',                                # ------
    "mk {item}":      "Make {item} in WD",               # V
    "rn {item}":      "Rename {item}",                   # V
    "rm {item}":      "Remove {item}",                   # V
    "rm -o ":         "Delete empty items in WD",        # V
    "cp {item}":      "Copy {item} to ...",              # V
    "mv {item}":      "Move {item} to ...",              # V
    "sd":             "Single Sort WD",                  # V
    "sd -r":          "Recursive Sort WD",               # V
    "op":             "Open WD",                         # V
    "rf":             "Refresh WD content",              # V
    "tp":             "Get type for every folder",       # V
    "hd":             "Set header",                       # V
    "clr":            "Get color for every item",        # V
    "fl ++ {val}":    "Increase fluency parameter",      # V
    "fl -- {val}":    "Decrease fluency parameter",      # V
    "{*item} >> exc": "Index {item} into exception",     # V
    "{*item} >> usd": "Index {item} into used",          # V
    "gt -d":          "Get dirs in WD",                  # V
    "gt -f":          "Get files in WD",                 # V
    ".......":        '',                                # ------
    # "-i exception": "Set Extension Directory",
    # "-ch step": "choose step",
}

req = {
    "cmd": {
        "help": "help",
        "undo": "undo",
        "exit": "fin",
        "mk": "make",
        "rn": "rename",
        "rm": "del",
        "cp": "copy",
        "mv": "move",
        "sd": "sort",
        "op": "open",
        "rf": "ref",
        "tp": "type",
        "hd": "header",
        "clr": "color",
        "ind": "ind",
        "fl": "fluency",
        "gt": "get",
    },
    "tag": {
        "++": "inc",
        "--": "dec",
        "-r": "rec",
        "-o": "odd",
        "-d": "dir",
        "-f": "file",
        "-t": "type",
    },
    "val": {
        "inc": 1,
        "dec": -1,
    }
}


def console(ui):
    def init_input():
        fin = ui.split() + ['']*(3 - len(ui.split()))
        if fin[0].isdigit():
            return ("ent", '', int(fin[0])) if not fin[1] else ("ind", fin[-1], (fin[:-2:]))
        else:
            _cmd, _tag = (req[kw].get(fin[j], '') for kw, j in zip(("cmd", "tag"), (0, 1)))
            if _cmd in ["fluency"]:
                _val = req["val"].get(_tag, '') if not fin[2] else fin[2]
            else:
                _val = ''
            _cmd = "ref" if not _cmd and ui.count(' ') == 0 and ui else _cmd
            _val = _val if _val else (fin[1] if not _tag else fin[2])
            return _cmd, _tag, _val

    cmd, tag, val = init_input()
    [print(k.ljust(32, ' '), v) if v else print('.' * 29 + k + '.' * 29) for k, v in help_req.items()] if ui == "help" else None
    val = val if cmd not in ["move", "copy", "del", "open", "make"] or tag else ui.split()[1::]
    val = int(val) if str(val).isdigit() else val
    if cmd in ["fluency"]:
        # val = 1 if not val else val
        # tag = tag if tag else req["val"][list(req["val"].values()).index(-1*(val < 0)*1)]
        val = 1 if not val else (abs(val)*req["val"][tag] if cmd == "fluency" else val)
        # val = val * req["val"][tag] if cmd == "fluency" else val
    if isinstance(val, list):
        for i in range(len(val)):
            val[i] = (int(val[i]) if val[i].isdigit() else val[i]) if val[i].count('-') == 0 else _to_i(val[i], int)
        val = _to_s(val)
    return cmd, tag, val


def start(*args, requester='', choicebox=True, reverse=False, color=_beige):
    val = args[1:] if len(args) > 1 else []
    if val:
        [print('-', x) for x in _to_s(val)]
    text = args[0].capitalize() if args[0].islower() else args[0]
    print(color + requester + color + text, '?', _box[0] * choicebox + _end)
    user_input = input(color + '>> ' + _end)
    true_return = ['y', "yes"] if reverse else ['', 'y', "yes"]
    if user_input in true_return:
        print(_grey + "<< yes" + _end)
        return True
    else:
        print(_grey + "<< no" + _end)
        return False


if __name__ == "__main__":
    # start("Well. Let's start")
    # start("Well. Let's start", reverse=True)
    console("help")
    print()
    for item in ['', "20", "rf", "13 >> exc", "1 2 3 >> usd", "rm 13", "rm -o", "mk folder", "mk folder_1 folder_2", "mk folder file.txt", "mv 1 23 5-7 16", "tp", "clr", "op", "op 7", "rn 3", "sd", "sd -r", "fl ++", "fl --", "fl", "fl -- 3", "hd", "fl -- 1", "gt -f", "gt -d"]:     # TODO: "fl -1"
        print(str({item}).ljust(32), console(item))
        _t.sleep(0.0)
    for k in range(0):
        print(console(input(">> ")))
