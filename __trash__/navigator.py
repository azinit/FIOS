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

_now = datetime.now
_type_dir, _color, _header, _fl = True, True, True, 1
MODE = "navigator"
correct, is_dir_clear = False, True
start = 0


# =====  Built-in  ===== #
def _set_time(step=0):
    global start

    if step == 0:
        start = _now()
    else:
        print(_f.grey + _f.bold + str(_now() - start) + _f.end)
        start = _now()


def _set_fluency(delta):
    global _fl
    _fl += delta


def _set_header(cmd, val=None):
    def __colorize_val(x):
        return _f.paint(x, _f.grey2)

    if cmd in ["type", "color", "fluency", "header", None]:
        val = [0] if val is None or isinstance(val[0], str) else val
        not_gen = cmd is not None
        arr = '⇛ '* not_gen
        dict_header = {
            "header":   ('🠶', " Header: %s%s"   % (arr, __colorize_val(_init(not_gen ^ _header, fl=_fl).switch.upper()))),
            "type":     ('📌', " Type: %s%s"     % (arr, __colorize_val(_init(not_gen ^ _type_dir, fl=_fl).switch.upper()))),
            "color":    ('👀', " Color: %s%s"    % (arr, __colorize_val(_init(not_gen ^ _color, fl=_fl).switch.upper()))),
            "fluency":  ('🚀', " Fluency: %s%s " % (arr, __colorize_val(_fl + val[0] * not_gen))),

        }
        if cmd is None:
            [_note.message_console(dict_header[x][1], c_pat=dict_header[x][0], color=_f.grey, c_pat_color=_f.grey2, end=_f.end + '  ') for x in ["type", "color", "header", "fluency"]]
            print()
        else:
            _note.message_console(dict_header[cmd][1], c_pat=dict_header[cmd][0], color=_f.grey, c_pat_color=_f.grey)


def _preparing(directory):
    """ Get, colorize and block items in path directory """
    _set_time(0)
    _exc, _usd = [_ind.get(x, fl=_fl) for x in [_ind.default_exc, _ind.default_used]]   # TODO: set/unset track
    sort_manager = False
    if is_dir_clear:
        if not op.exists(directory):
            i = 0
            while i < 3 and not op.exists(directory):
                directory = op.split(directory)[0]
                i += 1
            directory = "F:\Work\CODE\Projects\SortManager" if not op.exists(directory) else directory
            _set_time(1)
            _note.result(directory, None, "navigator", '', lambda x: _to_gp(x), end=' ', fl=_fl), _note.waiting(end=' ')
        dir_ = _hierarchy(directory, fl=_fl)  # _dir = sort.file_order(this_dir) # TODO: ValueError: too many values to unpack (expected 2)
        dir_.insert(0, _init(op.split(directory)[0], fl=_fl))
    else:
        sort_manager = True if r"F:\Work\CODE\Projects\SortManager\Sorted\System" in directory else False
        dir_ = [_init(x, fl=_fl) for x in directory]

    labels = ["🔝 toParent"] * is_dir_clear
    for i, x in enumerate(dir_):    # Colorize
        if i != 0 or not is_dir_clear:
            if x.type == "folder":
                if _type_dir:
                    if sort_manager:
                        item = _f.paint(_dirs[x.name][2] + ' ' + x.name, _dirs[x.name][0])
                        labels.append(item if _color else _f.paint(item, _f.bold, total=True))
                    else:
                        item = _f.paint(x.get_content_type(False) + ' ' + x.name, _f.bold)
                        labels.append(item if _color else _f.paint(item, _f.bold, total=True))
                else:
                    labels.append(_f.paint(x.sign + ' ' + x.name, _f.bold))
            else:
                color = str(_dirs[_fp.get(x.property, ["Unassigned"])[0]][0]) * _color
                labels.append(color + x.sign + _f.end + ' ' + x.name)
    """ Indexing items """
    labels = _ind.files(labels, dir_, _usd, _f.grey)[0]
    labels, _exc = _ind.files(labels, dir_, _exc, _f.red)   # TODO: ?+ labels = _ind.files(labels, dir_clear, invalid_ways, _f.red2)
    _set_time(1)
    return dir_, labels, _exc


def _get_correct_input(directory, fin, cur_dir, mod, _exc):
    """ Convert user_input to command, tags and values """
    # [False, True, None] == [Exit, GoNext, Refresh]    ||    "cmd": (flag, value),    ||    "cmd": func(*args),
    def __offset(x, check_list):
        print() if x in check_list else None

    def __set(value):
        return set(value) if isinstance(value, list) else {value}

    _set_time(0)
    """ Get cmd, tag, val """
    cmd, tag, val = _console(fin)
    __offset(cmd, ["rename", "del", "move", "copy", "open", "get", "make"])
    """ Init built-in vars """
    global correct
    temp0, temp1 = False, False
    cmd = "sort" if mod == "sort" and cmd in ['', "sort"] and not val else cmd
    correct = True if fin == "rf" or cmd and cmd != "ref" else False
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
        "header":   (None, "switch_hd"),
        "ind":      (None, ''),
        "fluency":  (None, ''),
        "get":      (None, ''),
        "cd":       (True, 0),
    }
    do = {
        "help":     (lambda x: input(">> ..")),
        "make":     (lambda x: _fm.create(op.join(directory, x), '', True)),
        "del":      (lambda x: _fm.delete(x, True)),
        "rename":   (lambda x: _fm.rename(x, input("Enter new name: "), True, 2)),
        "open":     (lambda x: _fm.open(x, True)),
        "get":      (lambda x: _subs(x, temp0, temp1, public=True, fl=_fl)),
        "ind":      (lambda x: _ind.append(op.join(_ind.dir_tmp, str(temp0)), x, public=True)),
        "fluency":  (lambda x: _set_fluency(x)),
    }
    """ Init cmd, tag, val """
    if cmd in out.keys():
        if cmd in ["move", "copy"]:     # TODO: if all are exc
            pathways, pathways_c, moved = [cur_dir[x] for x in val], [cur_dir[x].content for x in val], []
            msg = [_f.paint("Selected:", _f.yellow) + _f.paint('(' + cmd + ')', _f.grey)] + [_obj.get("element") + ' ' + p for p in _ind.files(pathways_c, pathways_c, _exc, _f.red)[0]]
            [print(x) for x in msg]
            inter = __set(pathways[0].family)
            for i in range(1, len(pathways)):
                inter &= __set(pathways[i].family)
            for sup_dst in list(inter):
                if sup_dst in _dirs:
                    _dst = _dirs[sup_dst]
                    dst_name_colored = _f.paint(_init(_dst[1], fl=_fl).sign + ' ' + _dst[1], _dst[0], '')
                    if _start("Is {0}{2}{1} the {0}destination{1}".format(_f.bold, _f.end, dst_name_colored), reverse=True, color=''):
                        r_dst = _dst[1]
                        break
            else:
                r_dst, msg = run([x[1] for x in _dirs.values()], 1, _f.yellow, cmd, False)
            print()
            for item in pathways:
                moved.append(op.join(r_dst, item.name))
                _fm.move(item.content, r_dst, public=True, exc=_exc, mod=cmd)
            out.update({cmd: (False, moved)})
        else:   # TODO: optimize for not common function; help by key_work cmd: fl -> ++/ -- ?
            """ INIT <val> """
            if cmd in ["fluency"]:
                val = [val]
            elif not val:
                val = [directory]
            else:
                val = [(cur_dir[x].content if isinstance(x, int) else x) for x in
                       (val if isinstance(val, list) else [val])]
            """ INIT <cmd> """
            """ "type", "color", "fluency", "header" """
            _set_header(cmd, val)
            """ "ind" """
            temp0 = _ind.used_tmp if cmd == "ind" and tag == "usd" else (_ind.exc_tmp if cmd == "ind" and tag == "exc" else temp0)
            """ "get" """
            temp0, temp1 = (True, False) if cmd == "get" and tag == "dir" else ((False, True) if cmd == "get" and tag == "file" else (temp0, temp1))
            """ "del" """
            out.update({cmd: (False, [x for x in val if x != directory])}) if cmd == "del" else None
            """ "sort -rec" """
            out.update({cmd: (False, "recursive")}) if cmd == "sort" and tag == "rec" else None
            """ "del - odd" """
            if cmd == "del" and tag == "odd":
                val = [x.content for x in cur_dir if x.property == "~/empty"]
                if not val:
                    _note.message_console("Nothing to delete ¯\_(ツ)_/¯ (or try to down fluency)", c_pat='', color=_f.grey)
                    cmd, tag, val = "ref", '', ''
            """ Do by <cmd> """
            [do.get(cmd)(x) for x in val] if cmd in do.keys() else None
    elif 0 <= val < len(cur_dir):
        if _fm._catch_exception(cur_dir[val].content, _exc, _f.grey):
            cmd = "ref"
        elif cur_dir[val].type == "file":
            cmd = "open"
            do.get("open")([directory] if not val else cur_dir[val].content)
        else:
            cmd = "cd"
            out.update({cmd: (True, val)})
    else:
        cmd = "ref"
    __offset(cmd, ["del", "move", "copy"]), _set_time(1)
    return out.get(cmd)


# =====   General  ===== #
# TODO: sort_file/folder_order, adv input, choose by mask (*.exe); .get => []
# TODO: sort delete incorrect path; v> fluency ~ folder_type/colorize; reset => std parameters; iterations into parameters
def run(directory, it=0, navi_color=_f.violet, mod="next", shutdown=True, dir_tp=_type_dir, color=_color, header=_header, fl=_fl):
    """ Navigator for File System with resolved operations such as move/copy/rename/delete and etc... """
    def __notify(step):
        if step == 0:
            _note.status(tag=MODE, color=navi_color, pattern='.') if it == 0 else print()
            if is_dir_clear:
                _note.result(directory, None, "cur_dir", '', _to_gp, general_c=navi_color, init=[True, ''], fl=fl),
                _set_header(None) if _header else None
                _note.message_console("Select %s location: " % _f.paint(mod, navi_color + _f.underline, navi_color), '', c_pat='', color=navi_color, end='')
            else:
                _note.result(_obj.get("folder"), True, "cur_dir", 'Choice', _to_gp, general_c=navi_color, init=['', ''], end=' ', fl=fl),
            _note.waiting(end=' ')
        elif step == 1:
            [print("{} {}".format(_f.paint(_dpw(i, str, 2)[0] + '.', navi_color), x)) for i, x in enumerate(cur_labels)]
        else:
            if flag:
                _note.result(cur_dir[k].content, None, MODE, decore=_to_gp, fl=fl)
            elif flag is None:
                None if correct else _note.result(fin, False, MODE, init=False, fl=fl)
            else:
                _note.parameters({"Iterations": it, "Final Path": directory}, color=navi_color + _f.bold + _f.underline, end='    ')
                None if not shutdown else _note.process(MODE, False, color=_f.bg(navi_color), fl=_fl)
                None if not shutdown else _note.status('.', '.', color=navi_color)
    global _type_dir, _color, _fl, is_dir_clear, _header
    _type_dir, _color, _fl, _header, is_dir_clear = dir_tp, color, fl, header, not isinstance(directory, list)
    __notify(0)
    cur_dir, cur_labels, exc = _preparing(directory)
    __notify(1)
    fin = input(">> ")  # TODO: waiting after input() : >> rf ⏳ ........ 0:00:00.076741
    flag, k = _get_correct_input(directory, fin, cur_dir, mod, exc)
    dir_tp, color, header = ((k == x) ^ y for x, y in zip(("switch_tp", "switch_cl", "switch_hd"), (dir_tp, color, header)))
    # input([flag, k])
    __notify(2)
    if flag:
        selected = cur_dir[k].content
        directory, k = run(selected, it + 1, navi_color, mod, shutdown, dir_tp, color, header, _fl)
    elif flag is None:
        directory, k = run(directory, it + 1, navi_color, mod, shutdown, dir_tp, color, header, _fl)
    return directory, k


if __name__ == "__main__":
    while True:
        sel_path, info = run(r"F:\Work\CODE\toStudy\Python", fl=5)
        print([sel_path, info])
    # TODO: mv 1 1 1 1 1 1 1 ....; mv -> *not inter* -> "enter"
    # sel_path = run([x[1] for x in _dirs.values()])
