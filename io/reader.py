from fios.io import console
from fios.util import fpath

THREAD_NAME = "READER"

# TODO: callback?
# TODO: Icon?
# TODO: Try?


# TODO: ?: readline(), read_int(), read_next(),
# TODO; add binary mode for media
# TODO: success?
def read(path, **kwargs):
    import os
    if path and os.path.exists(path):
        # init kwargs
        mode        = kwargs.get("mode",        "r")
        encoding    = kwargs.get("encoding",    "utf-8")
        notify      = kwargs.get("notify",      False)
        # read file
        with open(path, mode, encoding=encoding) as fin:
            content = fin.read()
        if notify: console.log(
            message="Read: {file}".format(file=fpath.cut(path)),
            thread=THREAD_NAME
        )
        return content


def readlines(path, **kwargs):
    # TODO: \r\n?
    remove_empty_rows = kwargs.get("remove_empty_rows", False)
    lines = read(path, **kwargs).split("\n")
    if remove_empty_rows:   lines = [l for l in lines if l != ""]
    return lines


if __name__ == '__main__':
    def __test__read():
        print(":::::::::::::::::::::read:::::::::::::::::::::")

    def __test__readlines():
        print(":::::::::::::::::::::readlines:::::::::::::::::::::")

    __test__read()
    __test__readlines()