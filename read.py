import os
import codecs

import FIOS.notifier as notifier


def from_file(filepath, public=False):
    path, name = os.path.split(filepath)
    content = ''
    if public:
        notifier.status()
        notifier.result(name, os.path.exists(filepath), "read")
        notifier.result(path, os.path.exists(path), "curdir")
    if os.path.exists(filepath):
        os.chdir(path)
        with codecs.open(name, 'r+', 'utf-8') as fin:
            content += fin.read()
        return content
