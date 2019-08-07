import os
import shutil
from typing import Union

from fios.io import console
# TODO: Callback for all

THREAD_NAME = "EXPLORER"


# TODO: relpath?
# TODO: + miniscripts? (pyinstaller, ui2py, ...)
"""
..............................................................................................................
................................................ BUILT-IN ....................................................
..............................................................................................................
"""

__map_match = {
    "undefined":    -1,
    "folder":       0,
    "file":         1,
}

# TODO: Rewrite
def __get_type(folder, file):
    """ Get type from kwargs: file or folder """
    is_valid = folder ^ file

    if folder and is_valid:
        return __map_match["folder"]
    elif file and is_valid:
        return __map_match["file"]
    else:
        return __map_match["file"]


def __is_valid(type_):
    return __is_file(type_) or __is_folder(type_)


def __is_folder(type_):
    return __map_match["folder"] == type_


def __is_file(type_):
    return __map_match["file"] == type_


"""
..............................................................................................................
................................................ METHOD SUMMARY ..............................................
..............................................................................................................
"""

"""
...................................................
.................... CREATE  ......................
...................................................
"""


def create(path, **kwargs):
    """ Create folder/file in directory """
    # TODO: already exist
    def __create_folder(path_):
        try:
            if os.path.exists(path_):
                return 2
            else:
                os.makedirs(path_)
                return 1
        except Exception as e:
            # console.log(e, thread=THREAD_NAME)
            return 0

    def __create__file(path_, content):
        try:
            if not os.path.exists(path_) or overwrite:
                directory = os.path.dirname(path_)
                if not os.path.exists(directory):
                    create(path=directory, folder=True)

                from fios.io import writer
                success = writer.write(path_, content)
                return success is not False
            else:
                return 2 if os.path.exists(path_) else 0
        except Exception as e:
            # console.log(e, thread=THREAD_NAME)
            return 0
    # init kwargs
    folder      = kwargs.get("folder",      False)
    file        = kwargs.get("file",        False)

    overwrite   = kwargs.get("overwrite",   False)
    content     = kwargs.get("content",     "")

    notify      = kwargs.get("notify",      False)
    type_       = __get_type(folder,        file)
    
    state       = 0

    # create items
    if __is_folder(type_):  state = __create_folder(path)
    if __is_file(type_):    state = __create__file(path, content)

    # notify
    if notify:
        from fios.util import fpath
        console.result(
            item=       fpath.cut(path),
            state=      state,
            patterns=   ["Creation failed: %s", "Created: %s", "Already exists: %s"],
            thread=     THREAD_NAME,
        )
    return state

def create_all(paths: list, **options):
    from fios.util.fdict import are_dict
    # TODO: are valid, options for every path?
    are_valid = True
    if are_valid:
        return [create(path, **options) for path in paths]
    else:
        return None

"""
...................................................
.................... RENAME  ......................
...................................................
"""


def rename(old: Union[bytes, str, os.PathLike], new: Union[bytes, str, os.PathLike], **kwargs):
    """ Rename folder/file in directory """
    notify          = kwargs.get("notify", False)
    IS_VALID_OLD    = os.path.exists(old)
    IS_VALID_NEW    = os.path.exists(os.path.dirname(new))

    if IS_VALID_OLD and IS_VALID_NEW:
        try:
            os.rename(old, new)
            state = 1
        except Exception as e:
            state = 0
            console.log(e, thread=THREAD_NAME)
    else:
        state = 2

    # notify
    if notify:
        from util import fpath
        console.result(
            item="{old} ↷ {new}".format(old=fpath.cut(old, **kwargs), new=fpath.cut(new, **kwargs)),
            state=state,
            patterns=["Renaming failed: %s", "Renamed: %s", "Invalid args: [%s]"],
            thread=THREAD_NAME,
        )
    return state


"""
...................................................
.................... DELETE  ......................
...................................................
"""


def delete(path: Union[bytes, str, os.PathLike], **kwargs):
    """ Delete folder/file in directory """
    def __delete__folder(path_):
        try:
            shutil.rmtree(path_, ignore_errors=ignore_errors)
            return True
        except Exception as e:
            console.log(e, thread=THREAD_NAME)
            return False

    def __delete__file(path_):
        try:
            os.remove(path_)
            return True
        except Exception as e:
            console.log(e, thread=THREAD_NAME)
            return False

    # init kwargs
    folder          = kwargs.get("folder",          False)
    file            = kwargs.get("file",            False)
    
    ignore_errors   = kwargs.get("ignore_errors",   True)
    notify          = kwargs.get("notify",          False)
    
    type_           = __get_type(folder,            file)
    state           = 0

    # delete items
    if __is_folder(type_):  state = __delete__folder(path)
    if __is_file(type_):    state = __delete__file(path)

    # notify
    if notify:
        from util import fpath
        console.result(
            item=fpath.cut(path, **kwargs),
            state=state,
            patterns=["Deleting failed: %s", "Deleted: %s"],
            thread=THREAD_NAME,
        )
    return state


"""
...................................................
.................... CLOSE  .......................
...................................................
"""


# TODO: close folder/file
def close(**kwargs):
    """ Close process/file/folder in os """
    # TODO: rewrite
    # item = _init(path, fl=fl)
    # success = False
    # if item.type == "file":
    #     os.system("TASKKILL /F /IM %s" % _files_p.get(item.property))
    #     success = True
    # _note.result(path, success, _mode()) if public else None
    # return success


"""
...................................................
.................... OPEN  ........................
...................................................
"""


# TODO: test on images, audio, ...
def open_(path, **kwargs):
    """ Open folder/file in Explorer """
    notify          = kwargs.get("notify", False)
    wait_message    = kwargs.get("wait_message", "...")

    # open
    try:
        os.startfile(path)
        if wait_message:    input(wait_message)        # TODO: Pause?
        state = 1
    except Exception as e:
        console.log(e, thread=THREAD_NAME)
        state = 0

    # notify
    if notify:
        from util import fpath
        console.result(
            item=fpath.cut(path, **kwargs),
            state=state,
            patterns=["Opening failed: %s", "Opened: %s"],
            thread=THREAD_NAME,
        )
    return state


"""
...................................................
.................... COPY  ........................
...................................................
"""


def copy(src: Union[bytes, str, os.PathLike], dst: Union[bytes, str, os.PathLike], **kwargs):
    """ Copy folder/file from-to """
    # TODO: enum if contains
    def __copy():
        # https://stackoverflow.com/a/1903753
        try:
            source_size = os.stat(__source_file).st_size
            copied = 0
            source = open(__source_file, 'rb')
            target = open(__target_file, 'wb')

            while True:
                chunk = source.read(32768)
                if not chunk:
                    break
                target.write(chunk)
                copied += len(chunk)

                callback()
                print('\r%02d%%' % (copied * 100 / source_size)),

            source.close()
            target.close()
            return True
        except Exception as e:
            console.log(e, thread=THREAD_NAME)
            return False

    # init kwargs
    callback    = kwargs.get("callback",    lambda x: None)
    notify      = kwargs.get("notify",      False)
    __patterns  = kwargs.get("__patterns",  ["Copying failed: %s", "Copied: %s", "Invalid args: [%s]"])

    IS_VALID_DST      = os.path.exists(src)
    IS_VALID_DST      = os.path.isdir(dst) and os.path.exists(dst)
    if IS_VALID_DST and IS_VALID_DST:
        # compute paths
        __filename          = os.path.split(src)[-1]
        __source_file   = src
        __target_file   = os.path.join(dst, __filename)

        NOT_ALREADY_EXIST = os.path.exists(__target_file)
        if NOT_ALREADY_EXIST:
            state = __copy()
        else:
            state = 2
    else:
        state = 2

    if notify:
        if notify:
            from util import fpath
            console.result(
                item="{dst} ⬅ {src}".format(src=fpath.cut(src, **kwargs), dst=fpath.cut(dst, **kwargs)),
                state=state,
                patterns=__patterns,
                thread=THREAD_NAME,
            )
        return state


"""
...................................................
.................... MOVE  ........................
...................................................
"""


def move(src: Union[bytes, str, os.PathLike], dst: Union[bytes, str, os.PathLike], **kwargs):
    """ Move folder/file from-to """
    state = copy(src, dst, __patterns=["Moving failed: %s", "Moved: %s", "Invalid args: [%s]"], **kwargs)
    if state == 1: delete(src)


"""
...................................................
.................... INFO ........................
...................................................
"""


def info(path: Union[bytes, str, os.PathLike]):
    # TODO: Extend?
    return os.stat(path)


def is_accessible(path: Union[bytes, str, os.PathLike]):
    try:
        with open(path, 'r+', encoding='utf-8') as file:
            return True
    except:
        return False


"""
...................................................
.................... VALIDATE  ....................
...................................................
"""


def validate(string, empty=False):
    prohibited = [
        ['\\', '∖'],
        ['/', '╱'],
        [':', '։'],
        ['?', '␦'],
        ['*', '⁕'],
        ['"', "''"],
        ['|', ' ⎸'],
        ['<', '≺'],
        ['>', '≻'],
        ['.', '.'],
        [',', ','],
    ]
    for char in prohibited:
        pattern = char[0]
        repl = char[1] if not empty else ""

        string = string.replace(pattern, repl)
    return string


"""
...................................................
.................... RENAME_PASSIVE ...............
...................................................
"""


def match(e: str, another_name: str):
    import os
    from fios.util import fpath
    directory, name             = os.path.split(os.path.abspath(e))
    if os.path.isdir(e):    ext = ""
    else:                   ext = fpath.file(name)["extension"]

    another_full_name   = '{name}{ext}'.format(
        name=another_name,
        ext= ('.%s' % ext) * (ext != "")
    )
    return os.path.join(directory, another_full_name)


"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    def __test__create():
        print(create)
        # create(r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my third\my fourth", public=True)


    def __test__rename():
        print("rename")
        rename("", "")
        # rename(r"C:\Users\Feebon\Desktop\Loops", "loli[pop", True)
        # rename(r"C:\Users\Feebon\Desktop\Fold", input("Enter new name "), True)
        # rename(r"C:\Users\Feebon\Desktop\123.png", input("Enter new name "), True)


    def __test__delete():
        print("delete")
        # delete(r"F:\Work\CODE\toStudy\Python\PyQt\converter.bat", True)


    def __test__close():
        print("close")
        # close("F:\Work\Lessons\Code\Iri\FB\input.txt")


    def __test__open():
        print("open")
        # open_("F:\Work\Lessons\Code\Iri\FB\input.txt")


    def __test__copy():
        print("copy")


    def __test__move():
        print("move")
        # move(r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my_file.bat",
        #      r"F:\Work\CODE\toStudy\Python\PyQt\my_second\my third", True, 4)
    
    def __test__info():
        print(":::::::::::::::::::::info:::::::::::::::::::::")
        info_ = info(__file__)
        print(info_)

    def __test__match():
        print(":::::::::::::::::::::match:::::::::::::::::::::")
        dir_ = os.path.dirname(os.path.abspath(__file__))
        print(os.path.abspath(__file__))
        print(match(e=__file__, another_name="LowPoly"))
        print()
        print(dir_)
        print(match(e=dir_, another_name="gta"))

        print()
        path = r"E:\__STORAGE__\2.WORK\(C) Other\Freelance\Orders\(__WIP__)\[PARSE] CaseParser\[GIT]\CaseParser\Portfolios\Pavel_Kapysk"
        print(path)
        print(match(e=path, another_name="Pavel_Kapysh"))


    def __test__access():
        print(":::::::::::::::::::::access:::::::::::::::::::::")
        # path = __file__
        path = r"C:\Users\Martis\Desktop\password_database(AutoRecovered).xlsx"
        path = r"C:\Users\Martis\Desktop\password_database(AutoRecovered).xlsx"
        print(is_accessible(path))

    __test__create()
    __test__rename()
    __test__delete()
    __test__close()
    __test__open()
    __test__copy()
    __test__move()
    __test__info()
    __test__match()
    __test__access()
