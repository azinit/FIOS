from datetime import datetime
import os
import re

import FIOS.cfg as cfg
import FIOS.sample as sample
import FIOS.convert as convert

files = convert.to_single_list(list(sample.files.values()))

class obj(object):
    def __init__(self, content, name='none'):
        self.content = content
        self.mpath = cfg.get(cfg.iCore, 'Paths', 'main')
        self.name, self.kind, self.type, self.ps = obj.data(self)
        self.path, self.string, self.time = content, content, content
        if name != 'none':
            self.name = name

    def data(self):
        # file: file.dict, file.dep
        # folder: common, dir.dict, dep.dict
        # string: name, line
        # number: time, date
        content = self.content

        def kind__(content_):
            if isinstance(content_, datetime):
                return 'time'
            elif str(content_).isdigit():
                return 'number'
            elif isinstance(content_, list):
                return 'array'
            elif isinstance(content_, bool):
                return 'boolean'
            elif isinstance(content_, dict):
                return 'dictionary'
            elif os.path.isabs(content_):
                if os.path.isfile(content_):
                    return 'file'
                elif os.path.isdir(content_):
                    return 'folder'
                else:
                    result = os.path.split(content_)[1]
                    result = re.findall(r'.\w+', result)
                    if result:
                        if result[1] in files:
                            return 'file'
                        else:
                            return 'folder'
                    else:
                        return 'folder'
            elif isinstance(content_, str):
                return 'string'

        def name__(content_, kind_):
            if kind_ == 'folder' or kind_ == 'file' or kind_ == 'path':
                return os.path.split(content_)[1]
            elif kind_ == 'number' or kind_ == 'time':
                return 'integer'
            elif kind_ == 'string':
                return 'Filename'
            elif kind_ == 'array':
                return 'List'
            elif kind_ == 'boolean':
                return 'Bool'
            else:
                return content_

        def type__(content_, name_, kind_):
            type_, subtype = 'none', ' '
            if kind_ == 'folder' or kind_ == 'file':
                if kind_ == 'folder':
                    dictionary = sample.dirs.copy()
                elif kind_ == 'file':
                    dictionary = sample.files.copy()
                else:
                    dictionary = {}
                # By types
                for value in dictionary.values():
                    for ext in value:
                        if name_.endswith(ext):
                            type_ = list(dictionary.keys())[list(dictionary.values()).index(value)]
                            break
                # By ierarchy
                # if len(files) > 50 and len(folder > 250 and level > 5 => longdirectory
                # if len(files) > 100 and len(folder > 500 and level > 7 => project
                # if len(files) > 500 and len(folder > 1000 and level > 10 => casefolder
                # irila(get.dirlevel(content))
                # files, dirs = list(get.subs(content, True, True))
                # lvl = get.dirlevel(content)
                pass
            elif kind_ == 'string':
                if len(content_.split()) > 1:
                    type_ = 'Line'
            return type_ + subtype

        def path__(kind_):
            if kind_ == 'folder' or kind_ == 'file':
                return 'path'
            else:
                return 'content'

        kind = kind__(content)
        name = name__(content, kind)
        tipe = type__(content, name, kind)
        path = path__(kind)
        return name, kind.capitalize(), tipe, path

    @classmethod
    def fi(cls, value):
        return cls(value, value)
