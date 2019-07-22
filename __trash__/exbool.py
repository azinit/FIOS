import os.path as op
import inspect


def xpath(x):
    FILE_PATH = inspect.stack()[1][1]
    CUR_PATH = op.dirname(FILE_PATH)
    return op.join(CUR_PATH, x)
