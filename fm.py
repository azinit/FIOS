import os
import os.path as op
import shutil
import codecs
import inspect

import FIOS.font as _f
import FIOS.notifier as _note
import FIOS.index as _ind
from FIOS.check import duplicate as _is_dup
from FIOS.sample import files_properties as _files_p
from FIOS.substance import init as _init
from FIOS.split import path as sp_path, file as sp_file


# =====  Built-in  ===== #
def _catch_exception(value, exc='', color=_f.red):
    exc = _ind.get(_ind.default_exc) if not exc else exc
    if value in exc:
        _note.message_console("⛔ %s: Exception ¯\_(ツ)_/¯" % sp_path(value, 2), c_pat='', color=color)
        return True
    else:
        return False


def _mode(delta=0):
    """ Define name for built-in-fm methods """
    return inspect.stack()[1+delta][3]


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
    _note.result(path, success, _mode()) if public else None
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
        _note.result(old, success, _mode(), new, lambda x: sp_path(x, branch_view), init=[item0.sign, True]) if public else None
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
        _note.result(path, success, _mode(), init=[item.sign, True]) if public else None
    return success


def clean():
    pass


# TODO: test on images, audio, ...
def open(path, public=False):
    """ Open selected file/folder by path """
    success = None
    if not _catch_exception(path):
        _note.result(path, success, _mode()) if public else None
        try:
            os.startfile(path)
            success = True
        except():
            success = False
        _note.result(path, success, _mode()) if public else None
    return success


# TODO: close folder, file...
def close(path, public=False):
    """ Close selected file/folder by path """
    item = _init(path)
    success = False
    if item.type == "file":
        os.system("TASKKILL /F /IM %s" % _files_p.get(item.property))
        success = True
    _note.result(path, success, _mode()) if public else None
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
                    shutil.move(source, destination) if mod == "move" else shutil.copy2(source, destination)
                    success = True
                except Exception as e:
                    print(_f.paint(e, _f.red)) if not ignore_errors else None

        _note.result(source, success, _mode(), destination, lambda x: sp_path(x, branch_view),
                     i_true=item_color, s_true=folder_color, init=[_src.sign, True]) if public else None
        return success


def copy(source, destination, public=False, branch_view=3, item_color=_f.blue, folder_color=_f.blue2, ignore_errors=False, exc=''):
    """ Copy file/folder to any destination by pathways """
    return move(source, destination, public, branch_view, item_color, folder_color, ignore_errors, mod="copy", exc=exc)


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
    src = [r"F:\Work\CODE\Projects\SortManager\toSort\chatClient\chatClient.exe",  r"F:\Work\CODE\Projects\SortManager\toSort\desktop\6.ZTL"]
    dst = [r"F:\Work\CODE\Projects\SortManager\Sorted\System", r"F:\Work\CODE\Projects\SortManager\Sorted\CG"]
    # move(src[1], dst[1], True)
