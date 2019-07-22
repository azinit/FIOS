import os
import codecs

from FIOS.notifier import status as _s, result as _r



def from_file(file_path, public=False):
    """ Read from file by path """
    path, name = os.path.split(file_path)
    content = ''
    if public:
        _s()
        _r(path, os.path.exists(path), "cur_dir")
        _r(file_path, os.path.exists(file_path), "read", decore=lambda x: os.path.split(x)[1])

    if os.path.exists(file_path):
        os.chdir(path)
        with codecs.open(name, 'r+', 'utf-8') as fin:
            content += fin.read()
        return content


def readline():
    # TODO: todo methods
    pass


def read_int():
    pass


def read_next():
    pass
