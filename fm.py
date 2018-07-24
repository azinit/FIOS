import os
import os.path as op
import shutil
import codecs
import inspect
import re

import FIOS.font as _f
import FIOS.notifier as _note
import FIOS.index as _ind
from FIOS.sample import objects as _obj, dirs as _dirs, files_properties as _files_p, MAIN_PATH as _MP
from FIOS.substance import init as _init
from FIOS.convert import to_graphic_path as _to_gp, _rld
from FIOS.get import subs as _subs
from FIOS.split import path as sp_path, file as sp_file
from FIOS.sort import hierarchy as _hierarchy
from FIOS.requester import console as _console, start as _start

correct = False


# =====   General  ===== #
def create(path, content="", public=False):
    """ Create new file/folder by path """
    item = _init(path)
    success = False
    if item.kind == "path" and not item.exist:
        if item.type in ["folder", "ambiguous"]:
            try:
                os.makedirs(path)
                success = True
            except Exception as e:
                print(_f.paint(e, _f.red))
        elif item.type == "file":
            if not os.path.exists(item.dir):
                create(item.dir)
            with codecs.open(path, "w", "utf-8") as my_file:
                my_file.write(content)
            success = True
        else:
            success = None
    _note.result(path, success, mode()) if public else None
    return success


def rename(old, new, public=False, branch_view=3):
    """ Rename exist file/ folder by path """
    item0, item1 = _init(old), _init(new)
    # print(str(item1))
    sign0 = item0.sign
    success = False
    if not item0.exist:
        success, new = None, ''
    else:
        try:
            new = op.join(item0.dir, str(item1.content)) if item1.kind in ["string", "number"] else new
            new += ('' if new.count('.') > 0 else '.' + item0.extension) if item0.type == "file" else ''
            os.rename(old, new)
            success = True
        except Exception as e:
            print(_f.paint(e, _f.red))
    _note.result(old, success, mode(), new, lambda x: sp_path(x, branch_view), init=[sign0, True]) if public else None
    return new if success else success


def delete(path, public=False, success=False):
    """ Delete exist file/ folder by path """
    if success is None:
        success = False
        path = "directory"
        init = False
    else:
        item = _init(path)
        sign = item.sign
        if not item.exist:
            success = None
        else:
            if item.type == "file":
                os.remove(path)
                success = True
            elif item.type == "folder":
                shutil.rmtree(path, True)
                success = True
            else:
                pass
        init = [sign, True]
    _note.result(path, success, mode(), init=init) if public else None
    return success


def clean():
    pass


# TODO: test on images, audio, ...
def open(path, public=False):
    """ Open selected file/folder by path """
    success = None
    _note.result(path, success, mode()) if public else None
    try:
        os.startfile(path)
        success = True
    except():
        success = False
    _note.result(path, success, mode()) if public else None
    return success


# TODO: close folder, file...
def close(path, public=False):
    """ Close selected file/folder by path """
    item = _init(path)
    success = False
    if item.type == "file":
        os.system("TASKKILL /F /IM %s" % _files_p.get(item.property))
        success = True
    _note.result(path, success, mode()) if public else None
    return success


def move(source, destination, public=False, branch_view=3, item_color=_f.blue, folder_color=_f.blue2, ignore_errors=False, mod="move"):
    """ Move file/folder to any destination by pathways """
    success, src, dst = False, _init(source), _init(destination)
    create(dst.content) if not dst.exist and src.exist else None
    # input(src)
    if not src.exist:
        success, destination = None, ''
    else:
        if op.exists(op.join(destination, src.name)):   # TODO: check (1)(2) ...; folders merger or inc index by input
            old, ext = sp_file(src.name)
            ext, res = ext if not ext else '.' + ext, re.findall("\d+", old)
            if res and str(old[-1:]).isdigit():
                digit = int(res[-1]) + 1
                new = _rld(old, digit-1)
            else:
                digit = 1
                new = old + "_%d" % digit
            while op.exists(op.join(destination, new + ext)):
                new = _rld(new, digit)
                digit += 1
            new_source = op.join(src.dir, new + ext)
            source = rename(source, new_source, branch_view=1)
            item_color = _f.yellow
        if source:
            try:
                os.chdir(destination)
                # shutil.move(source, destination) if mod == "move" else shutil.copy2(source, destination)
                success = True
            except Exception as e:
                print(_f.paint(e, _f.red)) if not ignore_errors else None

    _note.result(source, success, mode(), destination, lambda x: sp_path(x, branch_view),
                 i_true=item_color, s_true=folder_color, init=[src.sign, True]) if public else None
    return success


def copy(source, destination, public=False, branch_view=3, item_color=_f.blue, folder_color=_f.blue2, ignore_errors=False):
    """ Copy file/folder to any destination by pathways """
    return move(source, destination, public, branch_view, item_color, folder_color, ignore_errors, mod="copy")


# TODO: sortierarchy, adv input, colorize and bold; choose by mask (*.exe); .get => []
# TODO: sort delete incorrect path
def navigator(path, it=0, color=_f.violet, mod="next", shutdown=True):
    """ Navigator for File System with resolved operations such as move/copy/rename/delete and etc... """
    def preparing():
        exceptions, used = [_ind.get(op.join(_ind.dir_tmp, x)) for x in [_ind.exc_tmp, _ind.used_tmp]]
        # input(op.join(ind.dir_tmp, ind.used_tmp))     # TODO: block-red; set/unset track
        if clear_path:
            # this_dir = sort.file_order(this_dir) # TODO: ValueError: too many values to unpack (expected 2)
            # os.path.exists(path)
            dir_ = _hierarchy(path)
            dir_.insert(0, op.split(path)[0])
            dir_clear = [op.join(path, x) for x in dir_]
        else:
            dir_clear = list(path).copy()
        dir_ = [_init(x) for x in dir_clear]
        folders = [x.content for x in dir_ if x.type == "folder"]
        labels = ["🔝 toParent"]*clear_path + [x.sign + ' ' + x.name for i, x in enumerate(dir_) if i != 0 or not clear_path]
        labels = _ind.files(labels, dir_clear, used, _f.grey)
        labels = _ind.files(labels, dir_clear, exceptions, _f.red)
        labels = _ind.files(labels, dir_clear, folders, _f.bold)
        # labels = _ind.files(labels, dir_clear, invalid_ways, _f.red2)

        return dir_, labels

    def get_correct_input(c_fin):
        # [False, True, None] == [Exit, GoNext, Refresh]    ||    "cmd": (flag, value),    ||    "cmd": func(*args),
        cmd, tag, val = _console(c_fin)
        global correct
        temp0, temp1 = False, False
        cmd = "sort" if mod == "sort" and cmd in ['', "sort"] and not val else cmd
        correct = True if c_fin == "rf" or cmd and cmd != "ref" else False
        # input([cmd, tag, val])
        out = {
            "help":   (None, ''),
            "undo":   (None, ''),
            "fin":    (False, "exit"),
            "":       (False, ''),
            "make":   (None, ''),
            "rename": (None, ''),
            "del":    (False, []),
            "move":   (False, []),
            "copy":   (False, []),
            "sort":   (False, "single"),
            "open":   (None, ''),
            "ref":    (None, ''),
            "type":   (None, ''),
            "ind":  (None, ''),
            "get":    (None, ''),
            "cd":     (True, 0),
        }
        do = {
            "help":   (lambda x: input(">> ..")),
            "make":   (lambda x: create(op.join(path, x), '', True)),
            "del":    (lambda x: delete(x, True)),
            "rename": (lambda x: rename(x, input("Enter new name: "), True, 2)),
            "open":   (lambda x: open(x, True)),
            "get":    (lambda x: _subs(x, temp0, temp1, True)),
            "ind":    (lambda x: _ind.append(op.join(_ind.dir_tmp, str(temp0)), x, public=True))
        }

        if cmd in out.keys():
            if cmd in ["move", "copy"]:
                to_set = lambda value: set(value) if isinstance(value, list) else {value}
                pathways, moved = [cur_dir[x] for x in val], []
                msg = [_f.paint("Selected:", _f.yellow) + _f.paint('(' + cmd + ')', _f.grey)] + [_obj.get("element") + ' ' + p.content for p in pathways] + [' ']
                [print(x) for x in msg]
                inter = to_set(pathways[0].family)
                for i in range(1, len(pathways)):
                    inter &= to_set(pathways[i].family)
                for sup_dst in list(inter):
                    dst = _dirs.get(sup_dst)
                    dst_name_colored = _f.paint(_init(dst[1]).sign + ' ' + dst[1], dst[0], '')
                    if _start("Is {0}{2}{1} the {0}destination{1}".format(_f.bold, _f.end, dst_name_colored), reverse=True, color=''):
                        r_dst = dst[1]
                        break
                else:
                    r_dst, msg = navigator([x[1] for x in _dirs.values()], 1, _f.yellow, cmd, False)
                for item in pathways:
                    moved.append(op.join(r_dst, item.name))
                    move(item.content, r_dst, public=True) if cmd == "move" else copy(item.content, r_dst, public=True)
                out.update({cmd: (False, moved)})
            else:
                temp0 = _ind.used_tmp if cmd == "ind" and tag == "usd" else (_ind.exc_tmp if cmd == "ind" and tag == "exc" else temp0)                      # init "ind"
                temp0, temp1 = (True, False) if cmd == "get" and tag == "dir" else ((False, True) if cmd == "get" and tag == "file" else (temp0, temp1))    # init "get"
                out.update({cmd: (False, [cur_dir[x].content for x in val])}) if cmd == "del" else None                                                     # init "del"
                out.update({cmd: (False, "recursive")}) if cmd == "sort" and tag == "rec" else None                                                         # init "sort -rec"
                if cmd == "del" and tag == "odd":                                                                                                           # init "del -odd"
                    val = [x.content for x in cur_dir if x.property == "~/empty"]
                    if not val:
                        print("No empty folders ¯\_(ツ)_/¯")
                        cmd, tag, val = "ref", '', ''
                val = [path] if not val else [(cur_dir[x].content if isinstance(x, int) else x) for x in (val if isinstance(val, list) else [val])]
                [do.get(cmd)(x) for x in val] if cmd in do.keys() else None
        elif 0 <= val < len(cur_dir):
            cmd = "open" if cur_dir[val].type == "file" else "cd"
            do.get("open")([path] if not val else cur_dir[val].content) if cmd == "open" else out.update({cmd: (True, val)})
        else:
            cmd = "ref"
        return out.get(cmd)

    def notify(step):
        if step == 0:
            _note.status(delta=1, color=color, pattern='.') if it == 0 else print()
            if clear_path:
                _note.result(path, None, "cur_dir", '', lambda x: _to_gp(x), general_c=color, init=[True, '']),
                _note.message_console("Select %s location: " % _f.paint(mod, color + _f.underline, color), '', c_pat='', color=color, end='')
            else:
                _note.result(_obj.get("folder"), True, "cur_dir", 'Choice', lambda x: _to_gp(x), general_c=color, init=['', '']),
            _note.waiting()
        elif step == 1:
            [print("{} {}".format(_f.paint(str(i) + '.', color), x)) for i, x in enumerate(cur_labels)]
        else:
            if flag:
                _note.result(selected, None, mode(1), decore=lambda x: _to_gp(x))
            elif flag is None:
                None if correct else _note.result(fin, False, mode(1), init=False)
            else:
                _note.parameters({"Final Path": path, "Iterations": it}, color=color + _f.bold + _f.underline)
                None if not shutdown else _note.process(mode(1), False, color=_f.bg(color))
                None if not shutdown else _note.status('.', '.', color=color)

    clear_path = not isinstance(path, list)
    notify(0)
    cur_dir, cur_labels = preparing()
    notify(1)
    fin = input(">> ")
    flag, k = get_correct_input(fin)
    # input([flag, k])
    if flag:
        selected = cur_dir[k].content
        notify(2)
        path, k = navigator(selected, it + 1, color, mod)
    elif flag is None:
        notify(2)
        path, k = navigator(path, it + 1, color, mod)
    else:
        notify(2)
    return path, k


# =====  Built-in  ===== #
def mode(delta=0):
    """ Define name for built-in-fm methods """
    return inspect.stack()[1+delta][3]


# =====    PyQt    ===== #
def ui2py(path):
    """ Convert *.ui file to *.py """
    # TODO: open converter directly
    name, directory = sp_file(sp_path(path, 1))[0], sp_path(path, -1)
    code = "pyuic5.exe #.ui -o #.py".replace('#', name)
    converter = directory + r"\\" + "converter.bat"
    create(converter, code, True)
    open(directory)


# TODO: test on all combinations in explorer
if __name__ == "__main__":
    def test_fm():
        # ui2py(r"F:\Work\CODE\toStudy\Python\PyQt\MyApp.ui")
        # create(r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my third\my fourth", public=True)
        # move(r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my_file.bat",
        #     r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my third", True, 4)
        # open("F:\Work\Lessons\Code\Iri\FB\input.txt")
        # close("F:\Work\Lessons\Code\Iri\FB\input.txt")
        # note.time.sleep(1)
        # delete(r"F:\Work\CODE\toStudy\Python\PyQt\converter.bat", True)
        # rename(r"C:\Users\Feebon\Desktop\Loops", "loli[pop", True)
        rename(r"C:\Users\Feebon\Desktop\Fold", input("Enter new name "), True)
        rename(r"C:\Users\Feebon\Desktop\123.png", input("Enter new name "), True)

    # test_fm()
    # ui2py(r"F:\Work\CODE\toStudy\Python\PyQt\Poems.ui")
    while False:
        sel_path, info = navigator(r"F:\Work\CODE\toStudy\Python")
        print([sel_path, info])
    # sel_path = navigator([x[1] for x in smp.dirs.values()])
    src = [r"F:\Work\CODE\Projects\SortManager\toSort\chatClient\chatClient.exe",  r"F:\Work\CODE\Projects\SortManager\toSort\desktop\4.ZTL"]
    dst = [r"F:\Work\CODE\Projects\SortManager\Sorted\System", r"F:\Work\CODE\Projects\SortManager\Sorted\CG"]
    move(src[1], dst[1], True)
