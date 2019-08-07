__SEPARATOR = "\\"
# __SEP_EXTR = "/"

"""
..............................................................................................................
................................................ METHODS SUMMARY .............................................
..............................................................................................................
"""
def abspath(relpath):
    # TODO:
    pass


def validate(path):
    import os
    return os.path.abspath(path)


def decorate(path: str, **kwargs):
    """ Change path appearance """
    symb = kwargs.get("symb", ' ⟩⟩ ')
    return validate(path).replace(__SEPARATOR, symb)


def cut(path: str, level=2):
    """ Cut odd levels in path """

    # TODO: Console message?

    tokens = validate(path).split(__SEPARATOR)[-level:]
    return __SEPARATOR.join(tokens)


# TODO: REWRITE!!!
def _rld(string, digit, inc=1):
    """ Replace last digit in file/folder name for successful move """
    string = string.split(str(digit))
    return str(digit).join(string[:-1]) + str(digit + inc) + string[-1]


# TODO: rewrite!
def file(fullname):
    result = fullname.split('.')
    if len(result) == 1:
        filename, file_extension = result[0], ''
    elif len(result) == 2:
        filename, file_extension = result
    else:    # > 2
        filename, file_extension = '.'.join(result[:len(result) - 1:]), result[len(result) - 1]
    return {"name": filename, "extension": file_extension}


# # TODO: optimize, dev
# def file_order(directory, num_list=""):
#     directory = directory if isinstance(directory, list) else os.listdir(directory)
#     max_int = max([-1] + [int(by_num(x)[-1]) for x in directory if by_num(x)])
#     if max_int == -1:
#         return directory
#     else:
#         num_list, sorted_dir = [x for x in range(max_int)] if not num_list else num_list
#         num_list.sort()
#         for digit in num_list:
#             for j, element in enumerate(directory):
#                 num = by_num(element)
#                 if num:
#                     if digit == int(num[-1]):
#                         sorted_dir.append(element)
#                         directory.pop(j)
#         return sorted_dir

# TODO: validator / items.path ?
# def duplicate(source, destination, fl=_fl):
#     src = _init(source, fl=fl)
#     if op.exists(op.join(destination, src.name)):   # TODO: check (1)(2) ...; folders merger or inc index by input
#         old, ext = sp_file(src.name)
#         ext, res = ext if not ext else '.' + ext, re.findall("\d+", old)
#         if res and str(old[-1:]).isdigit():
#             digit = int(res[-1]) + 1
#             new = _rld(old, digit - 1)
#         else:
#             digit = 1
#             new = old + "_%d" % digit
#         while op.exists(op.join(destination, new + ext)) or op.exists(op.join(src.dir, new + ext)):
#             new = _rld(new, digit)
#             digit += 1
#         return op.join(src.dir, new + ext)
#     else:
#         return False

# def name(full_path):
#     path, fullname = os.path.split(full_path)
#     os.chdir(path)
#     lst = fullname.split('.')
#     if len(lst) > 2:
#         newname = ''
#         for i in range(0, len(lst) - 1):
#             newname += lst[i]
#         newname += '.' + (str(lst[len(lst) - 1])).lower()
#         if os.path.exists(os.path.join(path, fullname)):
#             os.rename(fullname, newname)
#         fullname = newname
#     return fullname


# # =====  File Sys  ===== #
# def subs(path, folders=True, files=False, public=False, recursive=True, color=_beige, fl=_fl):
#     def unite(main_dir, sub_list):
#         return list(map(lambda x: os.path.join(main_dir, x), sub_list))
#
#     _s(pattern='.', color=color) if public else None
#     dst, level = _init(path, fl=fl), 0
#     root = os.path.split(dst.content)[0] if dst.kind == 'file' else dst.content
#     if root:
#         result_files, result_folders = [], [root] if folders else []
#         for rootName, folderNames, fileNames in os.walk(root):
#             if not recursive and level > 0:
#                 break
#             if folders and recursive:
#                 result_folders.extend(unite(rootName, folderNames))
#             if files:
#                 result_files.extend(unite(rootName, fileNames))
#             level += 1
#         if public:
#             [print(_yellow, _init(x, fl=fl).sign, x, _end) for x in result_folders]
#             [print(_blue, _init(x, fl=fl).sign, x, _end) for x in result_files]
#         _s(tag='.', pattern='.', color=color) if public else None
#         if files and folders:
#             return result_folders, result_files
#         elif files:
#             return [], result_files
#         elif folders:
#             return result_folders, []
#         else:
#             return [], []
"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""


if __name__ == '__main__':
    def __test__decorate():
        print(":::::::::::::::::::::decorate:::::::::::::::::::::")
        print(decorate(__file__))


    def __test__cut():
        import os
        test_set = [
            r"F:\Work\CODE\toStudy\Python"
        ]
        print(":::::::::::::::::::::cut:::::::::::::::::::::")
        print(cut(__file__))
        print(cut(__file__, level=2))
        print(cut(__file__, level=1))
        print(cut(__file__, level=3))
        print(cut(test_set[0], level=3))
        print(cut(test_set[0], level=0))
        print(cut(test_set[0], level=1))
        print(cut(os.path.abspath(__file__), level=5))

    def __test__rld():
        print(":::::::::::::::::::::rld:::::::::::::::::::::")
        print(_rld(r"F:\Work\CODE\Projects\SortManager\toSort\desktop_2\leather_002_bitmap_2.sbsar", 2))
        print(_rld(r"leather_002_bitmap_2.sbsar", 2))

    def __test__file():
        print(":::::::::::::::::::::file:::::::::::::::::::::")
        print(file(fullname="sample"))
        print(file(fullname="sample.py"))
        print(file(fullname="sample.py.py"))
        p = r"E:\__STORAGE__\2.WORK\(C) Other\Freelance\Orders\(__WIP__)\[PARSE] CaseParser\[GIT]\CaseParser\Portfolios\Pavel_Kapysk"
        print(file(fullname=p))

    __test__decorate()
    __test__cut()
    __test__file()

    # print(duplicate(r"F:\Work\CODE\Projects\SortManager\toSort\desktop\13.mp3",
    #                 r"F:\Work\CODE\Projects\SortManager\Sorted\Audio"))

    # subs(path=_MP, folders=True, files=True, public=True, recursive=False)

