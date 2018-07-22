import shutil
import FIOS.get as get
import FIOS.notifier as note
import FIOS.split as split
import FIOS.sort as sort
import FIOS.index as ind
import FIOS.requester as req

subst, convert = note.subst, note.convert
f, smp = ind.font, subst.sample
os, op = ind.os, subst.op
codecs, inspect = ind.codecs, subst.inspect

correct = False


# =====   General  ===== #
def create(path, content="", public=False):
    item = subst.init(path)
    success = False
    if item.kind == "path" and not item.exist:
        if item.type in ["folder", "ambiguous"]:
            try:
                # os.makedirs(path)
                success = True
            except Exception as e:
                print(f.paint(e, f.red))
        elif item.type == "file":
            # if not os.path.exists(item.dir):
            #     create(item.dir)
            # with codecs.open(path, "w", "utf-8") as my_file:
                # my_file.write(content)
            #    pass
            success = True
        else:
            success = None
    note.result(path, success, mode()) if public else None
    return success


def rename(old, new, public=False, branch_view=3):
    item0, item1 = subst.init(old), subst.init(new)
    # print(str(item1))
    sign0 = item0.sign
    success = False
    if not item0.exist:
        success, new = None, ''
    else:
        try:
            new = op.join(item0.dir, str(item1.content)) if item1.kind in ["string", "number"] else new
            new += ('' if new.count('.') > 0 else '.' + item0.extension) if item0.type == "file" else ''
            # os.rename(old, new)
            success = True
        except Exception as e:
            print(f.paint(e, f.red))
    note.result(old, success, mode(), new, lambda x: split.path(x, branch_view), init=[sign0, True]) if public else None
    return success


def delete(path, public=False):
    item = subst.init(path)
    success = False
    if not item.exist:
        success = None
    else:
        if item.type == "file":
            # os.remove(path)
            success = True
        elif item.type == "folder":
            # shutil.rmtree(path, True)
            success = True
        else:
            pass
    note.result(path, success, mode()) if public else None
    return success


def clean():
    pass


# TODO: test on images, audio, ...
def open(path, public=False):
    success = None
    note.result(path, success, mode()) if public else None
    try:
        # os.startfile(path)
        success = True
    except():
        success = False
    note.result(path, success, mode()) if public else None
    return success


# TODO: close folder, file...
def close(path, public=False):
    item = subst.init(path)
    success = False
    if item.type == "file":
        os.system("TASKKILL /F /IM %s" % note.smp.files_properties.get(item.property))
        success = True
    note.result(path, success, mode()) if public else None
    return success


def move(source, destination, public=False, branch_view=3, item_color=f.blue, folder_color=f.blue2):
    src, dst = subst.init(source), subst.init(destination)
    success = False
    dst_are = create(dst.content) if not dst.exist else None
    if not src.exist:
        success, destination = None, ""
    elif not(dst.exist or dst_are):
        success, source, destination = None, destination, ""
    else:
        try:
            os.chdir(destination)
            # shutil.move(source, destination)
            success = True
        except Exception as e:
            print(f.paint(e, f.red))
    i, s = item_color, folder_color
    note.result(source, success, mode(), destination, lambda x: split.path(x, branch_view),
                i_true=i, s_true=s) if public else None
    return success


def copy(source, destination, public=False, branch_view=3, item_color=f.blue, folder_color=f.blue2):
    src, dst = subst.init(source), subst.init(destination)
    success = False
    dst_are = create(dst.content) if not dst.exist else None
    if not src.exist:
        success, destination = None, ""
    elif not(dst.exist or dst_are):
        success, source, destination = None, destination, ""
    else:
        try:
            os.chdir(destination)
            # shutil.copy2(source, destination)
            success = True
        except Exception as e:
            print(f.paint(e, f.red))
    i, s = item_color, folder_color
    note.result(source, success, "move", destination, lambda x: split.path(x, branch_view),
                i_true=i, s_true=s) if public else None
    return success


# TODO: sortierarchy, adv input, colorize and bold
def navigator(path, it=0, color=f.violet, mod="next", shutdown=True):
    # TODO: block-red; set/unset track
    def preparing():
        exceptions, used = [ind.get(op.join(ind.dir_tmp, x)) for x in [ind.exc_tmp, ind.used_tmp]]
        # input(op.join(ind.dir_tmp, ind.used_tmp))
        dir_ = sort.hierarchy(path)
        # this_dir = sort.file_order(this_dir) # TODO: ValueError: too many values to unpack (expected 2)
        # os.path.exists(path)
        if clear_path:
            dir_.insert(0, op.split(path)[0])
            dir_clear = [op.join(path, x) for x in dir_]
        else:
            dir_clear = path.copy()
        dir_ = [subst.init(x) for x in dir_clear]
        empty = [x.content for x in dir_ if x.type == "folder" and x.len == 0]
        labels = ["🔝 toParent"]*clear_path + [x.sign + ' ' + x.name for i, x in enumerate(dir_) if i != 0 or not clear_path]
        labels = ind.files(labels, dir_clear, used, f.underline)
        labels = ind.files(labels, dir_clear, exceptions, f.red)
        labels = ind.files(labels, dir_clear, empty)
        return dir_, labels, empty

    def get_correct_input(c_fin):
        # [False, True, None] == [Exit, GoNext, Refresh]    ||    "cmd": (flag, value),    ||    "cmd": func(*args),
        cmd, tag, val = req.console(c_fin)
        global correct
        temp0, temp1 = False, False
        cmd = "sort" if mod == "sort" and not val else cmd
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
            "sort":   (False, 'single'),
            "open":   (None, ''),
            "ref":    (None, ''),
            "type":   (None, ''),
            "ind":  (None, ''),
            "get":    (None, ''),
            "cd":     (True, 0),
        }
        do = {
            "make":   (lambda x: create(op.join(path, x), '', True)),
            "del":    (lambda x: delete(x, True)),
            "rename": (lambda x: rename(x, input("Enter new name: "), True, 2)),
            "open":   (lambda x: open(x, True)),
            "get":    (lambda x: get.subs(x, temp0, temp1, True)),
            "ind":  (lambda x: ind.append(op.join(ind.dir_tmp, str(temp0)), x, public=True))
        }

        if cmd in out.keys():
            if cmd in ["move", "copy"]:
                to_set = lambda value: set(value) if isinstance(value, list) else {value}
                pathways, moved = [cur_dir[x] for x in val], []
                msg = [f.paint("Selected:", f.yellow) + f.paint('(' + cmd + ')', f.grey)] + [smp.objects.get("element") + ' ' + p.content for p in pathways] + [' ']
                [print(x) for x in msg]
                inter = to_set(pathways[0].family)
                for i in range(1, len(pathways)):
                    inter &= to_set(pathways[i].family)
                for sup_dst in list(inter):
                    dst = smp.dirs.get(sup_dst)
                    dst_name_colored = f.paint(subst.init(dst[1]).sign + ' ' + dst[1], dst[0], '')
                    if req.start("Is {0}{2}{1} the {0}destination{1}".format(f.bold, f.end, dst_name_colored), reverse=True):
                        r_dst = dst[1]
                        break
                else:
                    r_dst, msg = navigator(path, 1, f.yellow, cmd, False)
                for item in pathways:
                    moved.append(op.join(r_dst, item.name))
                    move(item.content, r_dst, public=True) if cmd == "move" else copy(item.content, r_dst, public=True)
                out.update({cmd: (False, moved)})
            else:
                temp0 = ind.used_tmp if cmd == "ind" and tag == "usd" else (ind.exc_tmp if cmd == "ind" and tag == "exc" else temp0)                        # init "ind"
                temp0, temp1 = (True, False) if cmd == "get" and tag == "dir" else ((False, True) if cmd == "get" and tag == "file" else (temp0, temp1))    # init "get"
                out.update({cmd: (False, [cur_dir[x].content for x in val])}) if cmd == "del" else None                                                     # init "del"
                out.update({cmd: (False, tag)}) if cmd == "sort" and tag == "rec" else None

                val = cur_empty if cmd == "del" and tag == "odd" else val                                                                                   # init "del -odd"
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
            note.status(delta=1, color=color, pattern='.') if it == 0 else print()
            if clear_path:
                note.result(path, None, "cur_dir", '', lambda x: convert.to_graphic_path(x), general_c=color, init=[True, '']),
                note.message_console("Select %s location: " % f.paint(mod, color + f.underline, color), '', c_pat='', color=color, end='')
            else:
                note.result(smp.objects.get("folder"), True, "cur_dir", 'Choice', lambda x: convert.to_graphic_path(x), general_c=color, init=['', '']),
            note.waiting()
        elif step == 1:
            [print("{} {}".format(f.paint(str(i) + '.', color), x)) for i, x in enumerate(cur_labels)]
        else:
            if flag:
                note.result(selected, None, mode(1), decore=lambda x: convert.to_graphic_path(x))
            elif flag is None:
                None if correct else note.result(fin, False, mode(1), init=False)
            else:
                note.parameters({"Final Path": path, "Iterations": it}, color=color + f.bold + f.underline)
                None if not shutdown else note.process(mode(1), False, color=f.bg(color))
                None if not shutdown else note.status('.', '.', color=color)

    clear_path = not isinstance(path, list)
    notify(0)
    cur_dir, cur_labels, cur_empty = preparing()
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
    return inspect.stack()[1+delta][3]


# =====    PyQt    ===== #
def ui2py(path):
    # TODO: open converter directly
    name, directory = split.file(split.path(path, 1))[0], split.path(path, -1)
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
    # sel_path = navigator([x[1] for x in smp.dirs.values()])
