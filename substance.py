import os
import os.path as op
import inspect
import datetime as d

from FIOS.font import red2 as _red2, end as _end
from FIOS.sample import files as _files, files_properties as _files_p, dirs as _dirs, objects as _obj, types as _typ

# TODO: */ bug ; fluency parameter ; fluency only in methods not in class??! :(
kinds_dict = {
    lambda x, n, f: Flag.create(x, n, f):                                         lambda x: isinstance(x, (bool, type(None))),
    lambda x, n, f: Number.create(int(x) if isinstance(x, str) else x, n, f):     lambda x: isinstance(x, (int, float, complex)) or str(x).isdigit(),
    lambda x, n, f: DataStructure.create(x, n, f):                                lambda x: isinstance(x, (list, tuple, dict, set, frozenset)),
    lambda x, n, f: TimeData.create(x, n, f):                                     lambda x: isinstance(x, (d.date, d.time, d.datetime)),
    lambda x, n, f: Path.create(str(x).strip(), n, f):                            lambda x: op.isabs(str(x)) and str(x)[0] not in ['\\'[:1], '/'],
    lambda x, n, f: String.create(x, n, f):                                       lambda x: isinstance(x, str),
    lambda x, n, f: Substance.create(x, n, f):                                    lambda x: True
}


# TODO: define type of objects; __len__ and ...
class Substance(object):
    def __init__(self, content, name='', fluency=1):
        self.content = content
        self.fluency = fluency
        self.name = str(inspect.stack()[5][4][0]).lstrip().split(" = ")[0] if not name else name
        self.kind = str(inspect.stack()[3][4][0][20::]).split('.')[0]
        self.kind = self.kind[0].lower() + self.kind[1:]
        self.type = abs(self)
        self.property = + self
        self.sign = self[_obj]

    def __abs__(self):
        return str(type(self.content)).split("'")[1]

    # TODO: Overload
    def __str__(self):
        header = "Kind: {0}{2}{1}, Type: {0}{3}{1}, Property: {0}{4}{1}".format(_red2, _end, self.kind, self.type, self.property)
        content = "{4} {2}: {0}{3}{1}".format(_red2, _end, self.name, self.content, self.sign)
        return header + "\n" + content

    def __pos__(self):
        return None

    def __getitem__(self, dictionary):
        for item in [self.type, self.kind]:
            if item in dictionary.keys():
                return dictionary[item]
        else:
            return ""

    @classmethod
    def create(cls, value, name='', fluency=1):
        return cls(value, name, fluency)


class Flag(Substance):
    def __init__(self, value, name='', fluency=1):
        Substance.__init__(self, value, name, fluency)
        self.switch = (self.property == 0) * "off" + (self.property == 1) * "on"

    def __pos__(self):
        return 2 if self.content is None else int(self.content)


class Number(Substance):
    def __init__(self, value, name='', fluency=1):
        Substance.__init__(self, value, name, fluency)

    def __pos__(self):
        if self.type != "complex":
            return '+' * (self.content > 0) + '0' * (self.content == 0) + '-' * (self.content < 0)


# TODO: intersection x * y overload
class DataStructure(Substance):
    def __init__(self, value, name='', fluency=1):
        Substance.__init__(self, value, name, fluency)


class TimeData(Substance):
    def __init__(self, value, name='', fluency=1):
        Substance.__init__(self, value, name, fluency)

    def __abs__(self):
        return Substance.__abs__(self).split('.')[1]


class Path(Substance):
    def __init__(self, value, name='', fluency=1):
        # TODO: mb files/folder contains amount....; init family/property if has time for procount(arg=True); self.color
        Substance.__init__(self, value, op.split(value)[1], fluency)
        self.exist = op.exists(self.content)
        self.dir = op.split(value)[0]
        self.extension = None if len(self.name.split('.')) == 1 else self.name.split('.')[-1]
        self.family = ~ self

    def __abs__(self):
        if op.isdir(self.content):
            return "folder"
        elif op.isfile(self.content) or str(self.name).count('.') > 0 and str(self.name)[0] != '.':
            return "file"
        else:
            return "ambiguous"

    def __str__(self):
        header, content = Substance.__str__(self).split("\n")
        header += ", Family: {0}{4}{1}\nExist: {0}{2}{1}, Dir: {0}{3}/..{1}".format(
            _red2, _end, self.exist, self.dir.split(r'\\'[:1:])[-1], self.family)
        p_name, extra = ("Extension", self.extension) if self.type == "file" else (("Files amount", self.len) if self.type == "folder" else ("Extra", "-"))
        header += "\n** {3}: {0}{2}{1}".format(_red2, _end, extra, p_name)
        return header + "\n" + content

    def __pos__(self):
        def get_key(value, dictionary):
            for key, value_list in dictionary.items():
                value_list = value_list if isinstance(value_list, list) else list(value_list)
                if value in value_list:
                    return key
            else:
                return None

        if self.type == "file":
            extension = self.name.split('.')
            if self.fluency < 3:
                return None if len(extension) == 1 else get_key('.' + extension[-1].lower(), _files)
            else:
                return None
        elif self.type == "folder":
            if self.fluency < 2:
                families, all_files = list(_files.keys()), []
                for root, folders, files in os.walk(self.content):
                    all_files.extend([op.join(root, x) for x in files])
                self.len = len(all_files)
                if len(all_files) == 0:
                    return "~/empty"
                elif len(all_files) <= 150:
                    count = [0]*len(families)
                    for file in all_files:
                        file_family = init(file).property
                        ind = families.index(file_family) if file_family in families else -1
                        count[ind] = count[ind] + 1 * (ind != -1)
                    count, families = zip(*sorted(zip(count, families), reverse=True))
                    return families[:min(5, count.index(0)):]
                else:
                    return "~/DEEP"
            else:
                self.len = 313
                return None
        else:
            return None

    def __getitem__(self, dictionary=_obj):
        if self.type == "file" and self.property in _files_p:
            return _files_p[self.property][1]
            # return sign if self.type == 'file' else "{}({})".format(sample.objects.get("folder"), sign)
        elif self.type == "folder":
            if self.property == "~/empty":
                return dictionary["e_folder"]
            elif self.property == "~/DEEP":
                return dictionary["d_folder"]
            else:
                return dictionary["folder"]
        else:
            return Substance.__getitem__(self, dictionary)

    def __invert__(self):
        if self.type == "file":
            return _files_p.get(self.property, ["Unassigned"])[0]
        elif self.type == "folder":
            if 0 < self.len <= 300:

                return list(dict.fromkeys([_files_p.get(x, ["Unassigned"])[0] for i, x in enumerate(self.property) if i < 3]))
            else:
                return self.property
        else:
            return "Unassigned"

    def get_content_type(self, in_general=True, main_sign=True):
        if self.type == "folder":
            if self.fluency < 2:
                if self.property == "~/empty":
                    symbol = ''
                elif self.property == "~/DEEP":
                    symbol = '( .. )'
                elif self.family:
                    if in_general:
                        kind = _dirs[self.family[0]]
                        symbol = "( %s )" % (kind[0] + kind[2] + _end)
                    else:
                        signs = [_dirs[x][0] + _dirs[x][2] + _end for x in self.family]
                        symbol = "( %s )" % ' '.join(signs)
                else:
                    symbol = "( ❓ )"
                return (self.sign + ' ')*main_sign + symbol
            else:
                return _obj["folder"]
        else:
            return ''


# TODO: to_center, to_column; rus/eng/ambiguous
class String(Substance):
    def __init__(self, value, name='', fluency=1):
        Substance.__init__(self, value, name, fluency)

    def __abs__(self):
        if len(self.content) == 1:
            return "char"
        elif str(self.content).count("\n") > 0:
            return "text"
        else:
            return "line"


def init(unknown_substance, name='', fl=1):
    # print(_red2 + str([inspect.stack()[1][3], fl, unknown_substance]) + _end)    # !!! FOR DEBUG BY REQUESTS !!!
    for kind, match_condition in kinds_dict.items():
        if match_condition(unknown_substance):
            return kind(unknown_substance, name, fl)


if __name__ == "__main__":
    def test_cases(mode):
        for i, (right_answer, test_case) in enumerate(_typ.items()):
            user_answer = init(test_case, fl=2)
            if mode == 0:
                print(str(user_answer))
                # if user_answer.type == "folder":
                #    print(user_answer.get_content_type(False))
            else:
                user = user_answer.kind + "_" + user_answer.type
                user += "_" + str(user_answer.exist) if user_answer.kind == "path" else ""
                print("{}: {}".format(i, _red2 + str(test_case) + _end))
                print("Expected answer: %s" % _red2 + str(right_answer) + _end)
                print("User answer: {}".format(_red2 * (user == right_answer) + user + _end))
            print()
    start = d.datetime.now()
    # input(init(r"F:\Work\CODE\toStudy\Python\my_second"))
    test_cases(0)
    test_value = "Hello! I'm Iri :)"
    # print(init('\*'))    # TODO: too many values for unpack???
    values = [test_value, [test_value], None, r"F:\Work\CODE\Projects\SortManager\Sorted\Audio", "F:\Work\CODE\Projects\SortManager\TestType", "F:\Work\CODE", r"F:\Work\CODE\toStudy\Python\PyQt\converter.bat"]
    dirs = _dirs.values()
    # [print(init(content, 'item'), '\n') for content in values[::-1]]
    # print(sample.files_properties.get(init(values[-1]).property[0]))
    for item_i in dirs:
        Dir = init(item_i[1], fl=1)
        print(Dir)
        # print(Dir.get_content_type(False), '\n')
    finish = d.datetime.now()
    print(finish - start)
