def file(fullname):
    result = fullname.split('.')
    if len(result) == 1:
        filename, file_extension = result[0], ''
    elif len(result) == 2:
        filename, file_extension = result
    else:    # > 2
        filename, file_extension = '.'.join(result[:len(result) - 1:]), result[len(result) - 1]
    return filename, file_extension


def path(full_path, up_lvl=2):
    blocks = str(full_path).split(r"\\"[:1:])
    result = [x for i, x in enumerate(blocks) if i >= len(blocks) - up_lvl]
    return r"\\".join(result)


if __name__ == "__main__":
    print(file(fullname="sample"))
    print(file(fullname="sample.py"))
    print(file(fullname="sample.py.py"))
    print(path(full_path=r"F:\Work\CODE\toStudy\Python", up_lvl=3))
