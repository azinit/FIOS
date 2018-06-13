import os
import codecs

# import write


def from_file(filepath, public=False):
    path, name = os.path.split(filepath)
    content = ''
    # write.status(access=public)
    # write.notification(name, os.path.exists(filepath), access=public, mode='read')
    # write.notification(name, os.path.exists(path), access=public, mode='curdir')
    os.chdir(path)
    with codecs.open(name, 'r+', 'utf-8') as finput:
        content += (finput.read())
    return content
