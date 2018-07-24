import os
import os.path as op
import shutil
import codecs
import inspect

import FIOS.font as _f
import FIOS.notifier as _note
import FIOS.index as _ind
from FIOS.check import duplicate as _is_dup
from FIOS.sample import objects as _obj, dirs as _dirs, files_properties as _files_p
from FIOS.substance import init as _init
from FIOS.convert import to_graphic_path as _to_gp
from FIOS.get import subs as _subs
from FIOS.split import path as sp_path, file as sp_file
from FIOS.sort import hierarchy as _hierarchy
from FIOS.requester import console as _console, start as _start

correct = False


# =====  Built-in  ===== #
def _catch_exception(value, exc='', color=_f.red):
    exc = _ind.get(_ind.default_exc) if not exc else exc
    if value in exc:
        _note.message_console("%s: Exception ¯\_(ツ)_/¯" % sp_path(value, 2), c_pat='', color=color)
        return True
    else:
        return False


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
    success = False
    if not _catch_exception(old):
        item0, item1 = _init(old), _init(new)
        # print(str(item1))
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
        _note.result(old, success, mode(), new, lambda x: sp_path(x, branch_view), init=[item0.sign, True]) if public else None
    return new if success else success


def delete(path, public=False, success=False):
    """ Delete exist file/ folder by path """
    if not _catch_exception(path):
        item = _init(path)
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
        _note.result(path, success, mode(), init=[item.sign, True]) if public else None
    return success


def clean():
    pass


# TODO: test on images, audio, ...
def open(path, public=False):
    """ Open selected file/folder by path """
    success = None
    if not _catch_exception(path):
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


def move(source, destination, public=False, branch_view=3, item_color=_f.blue, folder_color=_f.blue2, ignore_errors=False, mod="move", exc=''):
    """ Move file/folder to any destination by pathways """
    success = False
    if not _catch_exception(source, exc) and not _catch_exception(destination, exc):
        _src, _dst = _init(source), _init(destination)
        create(_dst.content) if not _dst.exist and _src.exist else None
        # input(src)
        if not _src.exist:
            success, destination = None, ''
        else:
            new_source = _is_dup(source, destination)
            if new_source:
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
                     i_true=item_color, s_true=folder_color, init=[_src.sign, True]) if public else None
        return success


def copy(source, destination, public=False, branch_view=3, item_color=_f.blue, folder_color=_f.blue2, ignore_errors=False, exc=''):
    """ Copy file/folder to any destination by pathways """
    return move(source, destination, public, branch_view, item_color, folder_color, ignore_errors, mod="copy", exc=exc)


# TODO: sortierarchy, adv input, colorize and bold; choose by mask (*.exe); .get => []
# TODO: sort delete incorrect path
def navigator(path, it=0, color=_f.violet, mod="next", shutdown=True):
    """ Navigator for File System with resolved operations such as move/copy/rename/delete and etc... """
    def preparing():
        _exc, _usd = [_ind.get(op.join(_ind.dir_tmp, x)) for x in [_ind.exc_tmp, _ind.used_tmp]]
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
        labels = _ind.files(labels, dir_clear, _usd, _f.grey)[0]
        labels, _exc = _ind.files(labels, dir_clear, _exc, _f.red)
        labels = _ind.files(labels, dir_clear, folders, _f.bold)[0]
        # labels = _ind.files(labels, dir_clear, invalid_ways, _f.red2)

        return dir_, labels, _exc

    def get_correct_input(c_fin):
        offset = lambda x, list: print() if x in list else None
        # [False, True, None] == [Exit, GoNext, Refresh]    ||    "cmd": (flag, value),    ||    "cmd": func(*args),

        cmd, tag, val = _console(c_fin)
        offset(cmd, ["rename", "del", "move", "copy", "open", "get", "make"])
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
            "ind":    (None, ''),
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
                pathways, pathways_c, moved = [cur_dir[x] for x in val], [cur_dir[x].content for x in val], []
                msg = [_f.paint("Selected:", _f.yellow) + _f.paint('(' + cmd + ')', _f.grey)] + [_obj.get("element") + ' ' + p for p in _ind.files(pathways_c, pathways_c, exc, _f.red)[0]] + [' ']
                [print(x) for x in msg]
                inter = to_set(pathways[0].family)
                for i in range(1, len(pathways)):
                    inter &= to_set(pathways[i].family)
                for sup_dst in list(inter):
                    _dst = _dirs.get(sup_dst)
                    dst_name_colored = _f.paint(_init(_dst[1]).sign + ' ' + _dst[1], _dst[0], '')
                    if _start("Is {0}{2}{1} the {0}destination{1}".format(_f.bold, _f.end, dst_name_colored), reverse=True, color=''):
                        r_dst = _dst[1]
                        break
                else:
                    r_dst, msg = navigator([x[1] for x in _dirs.values()], 1, _f.yellow, cmd, False)
                print()
                for item in pathways:
                    moved.append(op.join(r_dst, item.name))
                    move(item.content, r_dst, public=True, exc=exc) if cmd == "move" else copy(item.content, r_dst, public=True, exc=exc)
                out.update({cmd: (False, moved)})
            else:
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
            if _catch_exception(cur_dir[val].content, exc, _f.grey):
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
                _note.result(cur_dir[k].content, None, mode(1), decore=lambda x: _to_gp(x))
            elif flag is None:
                None if correct else _note.result(fin, False, mode(1), init=False)
            else:
                _note.parameters({"Final Path": path, "Iterations": it}, color=color + _f.bold + _f.underline)
                None if not shutdown else _note.process(mode(1), False, color=_f.bg(color))
                None if not shutdown else _note.status('.', '.', color=color)

    clear_path = not isinstance(path, list)
    notify(0)
    cur_dir, cur_labels, exc = preparing()
    notify(1)
    fin = input(">> ")
    flag, k = get_correct_input(fin)
    # input([flag, k])
    notify(2)
    if flag:
        selected = cur_dir[k].content
        path, k = navigator(selected, it + 1, color, mod)
    elif flag is None:
        path, k = navigator(path, it + 1, color, mod)
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
    while True:
        sel_path, info = navigator(r"F:\Work\CODE\toStudy\Python")
        print([sel_path, info])
    # sel_path = navigator([x[1] for x in _dirs.values()])
    src = [r"F:\Work\CODE\Projects\SortManager\toSort\chatClient\chatClient.exe",  r"F:\Work\CODE\Projects\SortManager\toSort\desktop\6.ZTL"]
    dst = [r"F:\Work\CODE\Projects\SortManager\Sorted\System", r"F:\Work\CODE\Projects\SortManager\Sorted\CG"]
    # move(src[1], dst[1], True)
