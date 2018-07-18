import FIOS.write as write
import FIOS.read as read
import FIOS.font as font
note = write.notifier
substance = note.substance
os = read.os
codecs = read.codecs

dir_tmp = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp"
used_tmp = "used_branches.txt"
exc_tmp = "exc_branches.txt"


# =====    Extra   ===== #
def string(value, color=font.red2):
    return color + value + font.end


def content(value, pattern):
    res = []
    for i in range(len(str(value))):
        if str(value)[i] == pattern:
            res.append(i)
    return res if len(res) > 0 else -1


# =====   General   ===== #
def new(full_path, public=False):
    def create(path, content="", public=False):
        item = substance.init(path)
        success = False
        if item.kind == "path" and not item.exist:
            if item.type in ["folder", "ambiguous"]:
                try:
                    os.makedirs(path)
                    success = True
                except Exception as e:
                    print(font.paint(e, font.red))
            elif item.type == "file":
                if not os.path.exists(item.dir):
                    create(item.dir)
                with codecs.open(path, "w", "utf-8") as my_file:
                    my_file.write(content)
                success = True
            else:
                success = None
        note.result(path, success, "create") if public else None
        return success

    try:
        create(full_path, public=public)
    except Exception as e:
        print(e)


def append(data_path, *args, public=False):
    args = args[0] if isinstance(args[0], list) else args
    if not os.path.exists(data_path):
        new(data_path, public)
    write.to_file(data_path, '\n'.join(args) + '\n', 'a', public=public)


def get(data_path, mode="used", public=False):
    data_links = False, []
    try:
        data = substance.init(data_path)
        os.chdir(data.dir)
        data_links = read.from_file(data_path).split('\r\n')[:-1:]
    except Exception as e:
        print(e)
    note.message_console(os.path.split(data_path)[1], "reading...") if public else None
    for link in data_links:
        note.message_console(link, 'was %s.' % mode, substance.init(link).sign, font.grey) if public else None
    return data_links


def clean(data_path, public=False):
    success = False
    try:
        data = substance.init(data_path)
        os.chdir(data.dir)
        write.to_file(data_path, '')
        success = True
    except Exception as e:
        print(e)
    note.result(data_path, success, "clean") if public else None


def files(label_list, check_list, to_index_list, color=font.grey):
    index_list = []
    for index_path in to_index_list:
        if index_path in check_list:
            index_list.append(list(check_list).index(index_path))
    return [font.paint(x, color) if i in index_list else x for i, x in enumerate(label_list)]


if __name__ == "__main__":
    print(string(value="SomeString. Mark me. pleeease ^___^", color=font.beige))
    print(content(value="Hello. It's Me", pattern="'"))
    print(content(value=type("Hello. It's Me"), pattern="'"))
    # new(os.getcwd(), True)
    data = [r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\used_branches.txt",
            r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\%Temp\exc_branches.txt"]
    for i in range(2):
        append(data[i], ["1", "2", "3"], public=True)
        data_list = get(data[i], public=True) if i == 0 else get(data[i], "blocked", True)
        clean(data[i], True)
