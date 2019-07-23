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


def __get_type(**kwargs):
    """ Get type from kwargs: file or folder """
    folder  = kwargs.get("folder",  False)
    file    = kwargs.get("file",    False)
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
    def __create_folder(path_):
        try:
            os.makedirs(path_)
            return True
        except Exception as e:
            console.log(e, thread=THREAD_NAME)
            return False

    def __create__file(path_, **kwargs_):
        try:
            content = kwargs_.get("content", "")

            directory = os.path.dirname(path_)
            if not os.path.exists(directory):
                create(path=directory, folder=True)

            from fios.io import writer
            writer.write(path_, content)
            return True
        except Exception as e:
            console.log(e, thread=THREAD_NAME)
            return False
    # init kwargs
    notify      = kwargs.get("notify", False)
    type_       = __get_type(**kwargs)
    state       = 0

    # create items
    if __is_folder(type_):  state = __create_folder(path)
    if __is_file(type_):    state = __create__file(path, **kwargs)

    # notify
    if notify:
        from util import fpath
        console.result(
            item=       fpath.cut(path, **kwargs),
            state=      state,
            patterns=   ["Creation failed: %s", "Created: %s"],
            thread=     THREAD_NAME,
        )
    return state


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
    ignore_errors   = kwargs.get("ignore_errors", True)
    notify          = kwargs.get("notify", False)
    type_           = __get_type(**kwargs)
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
    notify = kwargs.get("notify", False)

    # open
    try:
        os.startfile(path)
        input("...")        # TODO: Pause?
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
.................... STAT  ........................
...................................................
"""


def info(path: Union[bytes, str, os.PathLike]):
    # TODO: Extend?
    return os.stat(path)


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
        print(":::info:::")
        info_ = info(__file__)
        print(info_)

    __test__create()
    __test__rename()
    __test__delete()
    __test__close()
    __test__open()
    __test__copy()
    __test__move()
    __test__info()
