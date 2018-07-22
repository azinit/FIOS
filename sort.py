import os
import re

import FIOS.substance as substance


# =====    DIGITS   ===== #
def by_num(value):
    return re.findall(r'\d+', value)


def by_interval(orig_list, ind_interval):
    insertion_list = []
    column = int(len(orig_list) / ind_interval)
    for i in range(0, ind_interval):
        for j in range(0, column):
            insertion_list.append(orig_list[i + j * ind_interval])
    return insertion_list


# =====    FILES   ===== #
'''def files_by_num(path, dirlist):
    if dirlist:
        return by_num(dirlist[0])
    else:
        return files_by_num(path, os.listdir(path))'''


# TODO: optimize, dev
def file_order(directory, num_list=""):
    directory = directory if isinstance(directory, list) else os.listdir(directory)
    max_int = max([-1] + [int(by_num(x)[-1]) for x in directory if by_num(x)])
    if max_int == -1:
        return directory
    else:
        num_list, sorted_dir = [x for x in range(max_int)] if not num_list else num_list
        num_list.sort()
        for digit in num_list:
            for j, element in enumerate(directory):
                num = by_num(element)
                if num:
                    if digit == int(num[-1]):
                        sorted_dir.append(element)
                        directory.pop(j)
        return sorted_dir


# TODO: optimize
def hierarchy(directory):
    sorted_hierarchy, i = [], 0
    if isinstance(directory, list):
        root = ''
        directory = directory.copy()
    else:
        root = directory
        directory = os.listdir(directory)
    while i != len(directory):
        element, el = directory[i], substance.init(os.path.join(root, directory[i]))
        if el.type == "folder":
            sorted_hierarchy.append(element)
            directory.pop(directory.index(element))
            i -= 1
        i += 1
    sorted_hierarchy.extend(directory)
    return sorted_hierarchy


if __name__ == "__main__":
    path_ = r'F:\Work\Lessons\Code\Iri\[dev]CreateTheory\vs 1.0\Planimetry\Triangles\Various\Formulas'
    sub = 'defin123ition4_1.txt'
    sub1 = 'definition1.txt'
    sub2 = 'defini1tion1.txt'
    print(by_num(sub))
    print(by_num(sub1))
    print(by_num(sub2))
    print(by_interval([x for x in range(1, 55)], 6))
    print(os.listdir(path_))
    print(file_order(path_))