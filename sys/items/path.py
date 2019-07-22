import os


class Path(object):
    def __init__(self, path):
        self.path   = path if os.path.isabs(path) else None
        self.exists = os.path.exists(path)
