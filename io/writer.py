from fios.io import console
from fios.util import fpath

THREAD_NAME = "WRITER"


# TODO: Icon?
# TODO: Try?
# TODO; add binary mode for media
# TODO: success?

# TODO: ? write.me(), write.list(), write.priority(),
def write(path: str, content: str, **kwargs):
    import os
    # if path and os.path.exists(path):
    if path and os.path.exists(os.path.split(path)[0]):
        # init kwargs
        mode        = kwargs.get("mode",        "w")
        encoding    = kwargs.get("encoding",    "utf-8")
        notify      = kwargs.get("notify",      False)
        # write file
        with open(path, mode, encoding=encoding) as fout:
            fout.write(content)

        if notify: console.log(
            message="Written: {file}".format(file=fpath.cut(path)),
            thread=THREAD_NAME
        )
        return content
    else:
        return False


def writelines(path: str, content: list, **kwargs):
    # TODO: \r\n?
    # TODO: success?
    # TODO: callback?
    joiner = kwargs.get("joiner", "\r\n")
    str_content = joiner.join(content)
    write(path, str_content, **kwargs)


if __name__ == '__main__':
    def __test__write():
        print(":::::::::::::::::::::write:::::::::::::::::::::")

    def __test__writelines():
        print(":::::::::::::::::::::writelines:::::::::::::::::::::")

    __test__write()
    __test__writelines()