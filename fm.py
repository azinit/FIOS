import shutil
import FIOS.notifier as note
import FIOS.split as split
import FIOS.sort as sort
import FIOS.index as ind
import FIOS.requester as req

font = ind.font
substance = note.substance
convert = note.convert
os = ind.os
op = substance.op
codecs = ind.codecs
inspect = substance.inspect


# =====   General  ===== #
def create(path, content="", public=False):
    item = substance.init(path)
    success = False
    if item.kind == "path" and not item.exist:
        if item.type in ["folder", "ambiguous"]:
            try:
                os.makedirs(path)
                success = True
            except Exception as e:
                print(font.paint(e, font.red))
        elif item.type == "file":
            if not os.path.exists(item.dir):
                create(item.dir)
            with codecs.open(path, "w", "utf-8") as my_file:
                my_file.write(content)
            success = True
        else:
            success = None
    note.result(path, success, mode()) if public else None
    return success


def rename(old, new, public=False, branch_view=3):
    item0, item1 = substance.init(old), substance.init(new)
    print(str(item1))
    success = False
    if not item0.exist:
        success, new = None, ''
    else:
        try:
            new = op.join(item0.dir, item1.content) if item1.kind == "string" else new
            os.rename(old, new)
            success = True
        except Exception as e:
            print(font.paint(e, font.red))
    note.result(old, success, mode(), new, lambda x: split.path(x, branch_view)) if public else None
    return success


def delete(path, public=False):
    item = substance.init(path)
    success = False
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
    note.result(path, success, mode()) if public else None
    return success


def clean():
    pass


# TODO: test on images, audio, ...
def open(path, public=False):
    success = None
    note.result(path, success, mode()) if public else None
    try:
        os.startfile(path)
        success = True
    except():
        success = False
    note.result(path, success, mode()) if public else None
    return success


# TODO: close folder, file...
def close(path, public=False):
    item = substance.init(path)
    success = False
    if item.type == "file":
        os.system("TASKKILL /F /IM %s" % note.smp.files_properties.get(item.property))
        success = True
    note.result(path, success, mode()) if public else None
    return success


def move(source, destination, public=False, branch_view=3):
    src, dst = substance.init(source), substance.init(destination)
    success = False
    dst_are = create(dst.content) if not dst.exist else None
    if not src.exist:
        success, destination = None, ""
    elif not(dst.exist or dst_are):
        success, source, destination = None, destination, ""
    else:
        try:
            os.chdir(destination)
            shutil.move(source, destination)
            success = True
        except Exception as e:
            print(font.paint(e, font.red))
    note.result(source, success, mode(), destination, lambda x: split.path(x, branch_view)) if public else None
    return success


def copy(source, destination, public=False):
    success = False
    note.result(source, success, "move", destination) if public else None


# TODO: sortierarchy, adv input, colorize
def navigator(path, it=0, color=font.violet):
    # TODO: block-red; set/unset track
    def preparing():
        this_dir = sort.hierarchy(path)
        # TODO: dev num_list, sorted_dir = [x for x in range(max_int)] if not num_list else num_list
        # this_dir = sort.file_order(this_dir) # TODO: ValueError: too many values to unpack (expected 2)
        this_dir.insert(0, op.split(path)[0])
        this_dir_full = list(map(lambda x: os.path.join(path, x), this_dir))
        exceptions, used = ind.get(op.join(ind.dir_tmp, ind.exc_tmp)), ind.get(op.join(ind.dir_tmp, ind.used_tmp))
        this_dir = [substance.init(op.join(path, x)) for x in this_dir]

        this_labels = ["🔝 toParent"] + [x.sign + ' ' + x.name for i, x in enumerate(this_dir) if i != 0]
        this_display = ind.files(this_labels, this_dir_full, used)
        this_display = ind.files(this_display, this_dir_full, exceptions, font.red)

        return this_dir, this_labels, this_display

    def get_correct_input(c_fin):
        # [False, True, None] == [Exit, GoNext, Refresh]
        if not req.console(c_fin.content):
            return False, None
        else:
            c_fin = c_fin.content if c_fin.kind == "number" and 0 <= c_fin.content < len(cur_dir) else None
            c_flag = True if (c_fin or c_fin == 0) else None
            return c_flag, c_fin

    def notify(step):
        if step == 0:
            note.status(delta=1, color=color, pattern='.'),
            note.result(path, os.path.exists(path), mode(1), '', lambda x: convert.to_graphic_path(x), color),
            note.message_console("Select next location: ", '', c_pat='', color=color),
        elif step == 1:
            [print("{} {}".format(font.paint(str(i) + '.', color), x)) for i, x in enumerate(cur_display)]
        else:
            if flag:
                note.result(selected, None, mode(1), decore=lambda x: convert.to_graphic_path(x)),
            elif flag is None:
                note.result(fin.content, False, mode(1)),
            else:
                note.parameters({"Final Path": path, "Iterations": it}, color=color + font.bold + font.underline)
                note.process(mode(1), False, color=font.bg(color))

    notify(0)
    cur_dir, cur_labels, cur_display = preparing()
    notify(1)
    fin = substance.init(input("> "))
    flag, k = get_correct_input(fin)
    if flag:
        selected = cur_dir[k].content
        notify(2)
        path = navigator(selected, it=it + 1)
    elif flag is None:
        notify(2)
        path = navigator(path, it=it + 1)
    else:
        notify(2)
        return path
    return path


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
        ui2py(r"F:\Work\CODE\toStudy\Python\PyQt\MyApp.ui")
        # create(r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my third\my fourth", public=True)
        move(r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my_file.bat",
             r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my third", True, 4)
        # open("F:\Work\Lessons\Code\Iri\FB\input.txt")
        # close("F:\Work\Lessons\Code\Iri\FB\input.txt")
        note.time.sleep(1)
        delete(r"F:\Work\CODE\toStudy\Python\PyQt\converter.bat", True)
        rename(r"C:\Users\Feebon\Desktop\Loops", "loli[pop", True)

    # test_fm()
    ui2py(r"F:\Work\CODE\toStudy\Python\PyQt\Poems.ui")
    # sel_path = navigator(r"F:\Work\CODE\toStudy\Python")
