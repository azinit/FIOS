import datetime as d
import os.path as path
import inspect

import FIOS.sample as sample
from FIOS.font import red2, end

# files_dict = to_single_list(list(files.values()))
kinds_dict = {
    lambda x, n: Boolean.create(x, n): lambda x: isinstance(x, bool),
    lambda x, n: Number.create(x, n): lambda x: isinstance(x, (int, float, complex)),
    lambda x, n: DataStructure.create(x, n): lambda x: isinstance(x, (list, tuple, dict, set, frozenset)),
    lambda x, n: DateTime.create(x, n): lambda x: isinstance(x, (d.date, d.time, d.datetime)),
    lambda x, n: Path.create(x, n): lambda x: path.isabs(str(x)),
    lambda x, n: String.create(x, n): lambda x: isinstance(x, str),
}


class Substance(object):
    def __init__(self, content, name=''):
        self.content = content
        self.name = str(inspect.stack()[5][4][0]).lstrip().split(" = ")[0] if not name else name
        self.kind = 'substance'
        self.type = abs(self)
        self.property = + self

    def __abs__(self):
        return str(type(self.content)).split("'")[1]
    # TODO
    # overload

    def __str__(self):
        header = "Kind: {0}{2}{1}, Type: {0}{3}{1}, Property: {0}{4}{1}".format(red2, end, self.kind, self.type, self.property)
        content = "> {2}: {0}{3}{1}".format(red2, end, self.name, self.content)
        return header + "\n" + content

    def __pos__(self):
        return None

    @classmethod
    def create(cls, value, name=''):
        return cls(value, name)


class Boolean(Substance):
    def __init__(self, value, name=''):
        Substance.__init__(self, value, name)
        self.kind = "boolean"


class Number(Substance):
    def __init__(self, value, name=''):
        Substance.__init__(self, value, name)
        self.kind = "number"

    def __pos__(self):
        if self.type != "complex":
            return '+' * (self.content > 0) + '0' * (self.content == 0) + '-' * (self.content < 0)


class DataStructure(Substance):
    def __init__(self, value, name=''):
        Substance.__init__(self, value, name)
        self.kind = "dataStructure"


class DateTime(Substance):
    def __init__(self, value, name=''):
        Substance.__init__(self, value, name)
        self.kind = "datetime"

    def __abs__(self):
        return Substance.__abs__(self).split('.')[1]


class Path(Substance):
    def __init__(self, value, name=''):
        Substance.__init__(self, value, path.split(value)[1] if not name else name)
        self.kind = "path"
        self.exist = path.exists(self.content)

    def __abs__(self):
        if path.isfile(self.content) or str(self.name).count('.') > 0:
            return "file"
        elif path.isdir(self.content):
            return "folder"
        else:
            return "ambiguous_path"

    def __str__(self):
        header, content = Substance.__str__(self).split("\n")
        header += ", Exist: {0}{2}{1}".format(red2, end, self.exist)
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
            extension = '.' + str(self.name.split('.')[1])
            return get_key(extension, sample.files)
        elif self.type == "folder":
            # TODO
            # return get_key(self.content, sample.dirs)
            return self.name
        else:
            return None


class String(Substance):
    def __init__(self, value, name=''):
        Substance.__init__(self, value, name)
        self.kind = "string"

    def __abs__(self):
        if len(self.content) == 1:
            return "char"
        elif str(self.content).count("\n") > 0:
            return "text"
        else:
            return "line"


def initialize(unknown_substance, name=''):
    for kind, match_condition in kinds_dict.items():
        if match_condition(unknown_substance):
            return kind(unknown_substance, name)


if __name__ == "__main__":
    def test_cases(mode):
        for i, (right_answer, test_case) in enumerate(sample.types.items()):
            user_answer = initialize(test_case)
            if mode == 0:
                print(str(user_answer))
            else:
                user = user_answer.kind + "_" + user_answer.type
                user += "_" + str(user_answer.exist) if user_answer.kind == "path" else ""
                print("{}: {}".format(i, red2 + str(test_case) + end))
                print("Expected answer: %s" % red2 + str(right_answer) + end)
                print("User answer: {}".format(red2 * (user == right_answer) + user + end))
            print()

    test_cases(1)
    value = "Hello! I'm Iri :)"
    item1 = initialize(value)
    item2 = initialize([value])
    print(str(item1))
    print(str(item2))
