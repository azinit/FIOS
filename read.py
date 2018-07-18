import os
import codecs

import FIOS.notifier as notifier


def from_file(file_path, public=False):
    path, name = os.path.split(file_path)
    content = ''
    if public:
        notifier.status()
        notifier.result(path, os.path.exists(path), "cur_dir")
        notifier.result(file_path, os.path.exists(file_path), "read", decore=lambda x: os.path.split(x)[1])

    if os.path.exists(file_path):
        os.chdir(path)
        with codecs.open(name, 'r+', 'utf-8') as fin:
            content += fin.read()
        return content

