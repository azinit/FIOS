import os.path as op
import time as _t
from datetime import datetime

import FIOS.font as _f
import FIOS.fm as _fm
import FIOS.notifier as _note
import FIOS.index as _ind
from FIOS.sample import dirs as _dirs, objects as _obj, files_properties as _fp
from FIOS.substance import init as _init
from FIOS.get import subs as _subs
from FIOS.convert import to_graphic_path as _to_gp
from FIOS.check import digits_by_pow as _dpw
from FIOS.sort import hierarchy as _hierarchy
from FIOS.requester import console as _console, start as _start


MODE = "navigator"
correct = False
_now = datetime.now


# =====  Built-in  ===== #
def _preparing(path, clear_path, folder_type, colorize, fluency):
    """ Get, colorize and block items in path directory """
    start = _now()
    _exc, _usd = [_ind.get(op.join(_ind.dir_tmp, x)) for x in [_ind.exc_tmp, _ind.used_tmp]]
    # input(op.join(ind.dir_tmp, ind.used_tmp))     # TODO: block-red; set/unset track
    if clear_path:
        if not op.exists(path):
            i = 0
            while i < 3 and not op.exists(path):
                path = op.split(path)[0]
                i += 0
            if not op.exists(path):
                path = "F:\Work\CODE\Projects\SortManager"
            print(_f.grey + _f.bold + str(_now() - start) + _f.end)
            _note.result(path, None, "navigator", '', lambda x: _to_gp(x), end=' '), _note.waiting(end=' ')

        dir_ = _hierarchy(path)  # _dir = sort.file_order(this_dir) # TODO: ValueError: too many values to unpack (expected 2)
        dir_.insert(0, op.split(path)[0])
        dir_clear = [op.join(path, x) for x in dir_]
    else:
        dir_clear = list(path).copy()

    dir_ = [_init(x, fluency=fluency) for x in dir_clear]
    labels = ["🔝 toParent"] * clear_path
    for i, x in enumerate(dir_):    # Colorize
        if i != 0 or not clear_path:
            if x.type == "folder":
                if folder_type:
                    item = _f.bold + x.get_content_type(False, False) + ' ' + x.name + _f.end
                    labels.append(item if colorize else _f.paint(item, _f.bold))
                else:
                    labels.append(_f.bold + x.sign + ' ' + x.name + _f.end)
            else:
                color = (_dirs[_fp.get(x.property, ["Unassigned"])[0]][0])*colorize
                labels.append(color + x.sign + _f.end + ' ' + x.name)

    labels = _ind.files(labels, dir_clear, _usd, _f.grey)[0]
    labels, _exc = _ind.files(labels, dir_clear, _exc, _f.red)
    # labels = _ind.files(labels, dir_clear, invalid_ways, _f.red2)
    print(_f.grey + _f.bold + str(_now() - start) + _f.end)
    return dir_, labels, _exc


def _get_correct_input(c_fin, mod, path, cur_dir, exc, folder_type, colorize, fluency):
    """ Convert user_input to command, tags and values """
    # [False, True, None] == [Exit, GoNext, Refresh]    ||    "cmd": (flag, value),    ||    "cmd": func(*args),
    def offset(x, check_list):
        print() if x in check_list else None

    cmd, tag, val = _console(c_fin)
    offset(cmd, ["rename", "del", "move", "copy", "open", "get", "make"])
    global correct
    temp0, temp1 = False, False
    cmd = "sort" if mod == "sort" and cmd in ['', "sort"] and not val else cmd
    correct = True if c_fin == "rf" or cmd and cmd != "ref" else False
    # input([cmd, tag, val])
    out = {
        "help":     (None, ''),
        "undo":     (None, ''),
        "fin":      (False, "exit"),
        "":         (False, ''),
        "make":     (None, ''),
        "rename":   (None, ''),
        "del":      (False, []),
        "move":     (False, []),
        "copy":     (False, []),
        "sort":     (False, "single"),
        "open":     (None, ''),
        "ref":      (None, ''),
        "type":     (None, "switch_tp"),
        "color":    (None, "switch_cl"),
        "ind":      (None, ''),
        "fluency":  (None, ''),
        "get":      (None, ''),
        "cd":       (True, 0),
    }
    do = {
        "help":     (lambda x: input(">> ..")),
        "make":     (lambda x: _fm.create(op.join(path, x), '', True)),
        "del":      (lambda x: _fm.delete(x, True)),
        "rename":   (lambda x: _fm.rename(x, input("Enter new name: "), True, 2)),
        "open":     (lambda x: _fm.open(x, True)),
        "get":      (lambda x: _subs(x, temp0, temp1, True)),
        "ind":      (lambda x: _ind.append(op.join(_ind.dir_tmp, str(temp0)), x, public=True))
    }

    if cmd in out.keys():
        if cmd in ["move", "copy"]:     # TODO: if all are exc
            to_set = lambda value: set(value) if isinstance(value, list) else {value}
            pathways, pathways_c, moved = [cur_dir[x] for x in val], [cur_dir[x].content for x in val], []
            msg = [_f.paint("Selected:", _f.yellow) + _f.paint('(' + cmd + ')', _f.grey)] + [_obj.get("element") + ' ' + p for p in _ind.files(pathways_c, pathways_c, exc, _f.red)[0]]
            [print(x) for x in msg]
            inter = to_set(pathways[0].family)
            for i in range(1, len(pathways)):
                inter &= to_set(pathways[i].family)
            for sup_dst in list(inter):
                if sup_dst in _dirs:
                    _dst = _dirs[sup_dst]
                    dst_name_colored = _f.paint(_init(_dst[1], fluency=fluency).sign + ' ' + _dst[1], _dst[0], '')
                    if _start("Is {0}{2}{1} the {0}destination{1}".format(_f.bold, _f.end, dst_name_colored), reverse=True, color=''):
                        r_dst = _dst[1]
                        break
            else:
                r_dst, msg = run([x[1] for x in _dirs.values()], 1, _f.yellow, cmd, False)
            print()
            for item in pathways:
                moved.append(op.join(r_dst, item.name))
                _fm.move(item.content, r_dst, public=True, exc=exc, mod=cmd)
            out.update({cmd: (False, moved)})
        else:   # optimize for not common function
            _note.message_console("👀 Type: %s" % _init(not folder_type, fluency=fluency).switch.upper(), c_pat='', color=_f.grey) if cmd == "type" else None
            _note.message_console("👀 Color: %s " % _init(not colorize, fluency=fluency).switch.upper(), c_pat='', color=_f.grey) if cmd == "color" else None
            temp0 = _ind.used_tmp if cmd == "ind" and tag == "usd" else (_ind.exc_tmp if cmd == "ind" and tag == "exc" else temp0)                      # init "ind"
            temp0, temp1 = (True, False) if cmd == "get" and tag == "dir" else ((False, True) if cmd == "get" and tag == "file" else (temp0, temp1))    # init "get"
            out.update({cmd: (False, [cur_dir[x].content for x in val])}) if cmd == "del" else None                                                     # init "del"
            out.update({cmd: (False, "recursive")}) if cmd == "sort" and tag == "rec" else None                                                         # init "sort -rec"
            if cmd == "del" and tag == "odd":                                                                                                           # init "del -odd"
                val = [x.content for x in cur_dir if x.property == "~/empty"]
                if not val:
                    _note.message_console("Nothing to sort ¯\_(ツ)_/¯", c_pat='', color=_f.grey)
                    cmd, tag, val = "ref", '', ''

            val = [path] if not val else [(cur_dir[x].content if isinstance(x, int) else x) for x in (val if isinstance(val, list) else [val])]
            [do.get(cmd)(x) for x in val] if cmd in do.keys() else None
    elif 0 <= val < len(cur_dir):
        if _fm._catch_exception(cur_dir[val].content, exc, _f.grey):
            cmd = "ref"
        elif cur_dir[val].type == "file":
            cmd = "open"
            do.get("open")([path] if not val else cur_dir[val].content)
        else:
            cmd = "cd"
            out.update({cmd: (True, val)})
    else:
        cmd = "ref"
    offset(cmd, ["del", "move", "copy"])
    return out.get(cmd)


# =====   General  ===== #
# TODO: sortierarchy, adv input, choose by mask (*.exe); .get => []
# TODO: sort delete incorrect path; arrange args; fluency ++/-- param; fluency ~ folder_type/colorize
def run(path, it=0, color=_f.violet, mod="next", shutdown=True, folder_type=False, colorize=True, fluency=1):
    """ Navigator for File System with resolved operations such as move/copy/rename/delete and etc... """
    def notify(step, c_path=''):
        if step == 0:
            _note.status(tag=MODE, color=color, pattern='.') if it == 0 else print()
            if clear_path:
                _note.result(path, None, "cur_dir", '', lambda x: _to_gp(x), general_c=color, init=[True, '']),
                _note.message_console("Select %s location: " % _f.paint(mod, color + _f.underline, color), '', c_pat='', color=color, end='')
            else:
                _note.result(_obj.get("folder"), True, "cur_dir", 'Choice', lambda x: _to_gp(x), general_c=color, init=['', ''], end=' '),
            _note.waiting(end=' ')
        elif step == 1:
            [print("{} {}".format(_f.paint(_dpw(i, str, 2)[0] + '.', color), x)) for i, x in enumerate(cur_labels)]
        else:
            if flag:
                _note.result(cur_dir[k].content, None, MODE, decore=lambda x: _to_gp(x))
            elif flag is None:
                None if correct else _note.result(fin, False, MODE, init=False)
            else:
                _note.parameters({"Iterations": it, "Final Path": path}, color=color + _f.bold + _f.underline, end='    ')
                None if not shutdown else _note.process(MODE, False, color=_f.bg(color))
                None if not shutdown else _note.status('.', '.', color=color)

    clear_path = not isinstance(path, list)
    notify(0)
    cur_dir, cur_labels, exc = _preparing(path, clear_path, folder_type, colorize, fluency)
    notify(1)
    fin = input(">> ")
    flag, k = _get_correct_input(fin, mod, path, cur_dir, exc, folder_type, colorize, fluency)
    folder_type, colorize = (k == "switch_tp") ^ folder_type, (k == "switch_cl") ^ colorize
    # input([flag, k])
    notify(2)
    if flag:
        selected = cur_dir[k].content
        path, k = run(selected, it + 1, color, mod, shutdown, folder_type, colorize)
    elif flag is None:
        path, k = run(path, it + 1, color, mod, shutdown, folder_type, colorize)
    return path, k


if __name__ == "__main__":
    while True:
        sel_path, info = run(r"F:\Work\CODE\toStudy\Python")
        print([sel_path, info])
    # TODO: mv 1 1 1 1 1 1 1 ....; mv -> *not inter* -> "enter"
    # sel_path = navigator([x[1] for x in _dirs.values()])
