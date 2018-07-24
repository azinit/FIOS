import os.path
import sys
import iri
import fm
# iri.launch()

# TODO: test to PythonStudy
# TODO: to_list (substance or convert) - list(val) if not list else val

def test_sort():
    list_1 = [5, 4, 3, 2, 1]
    list_2 = ['a', 'l', 'i', 'r', 'i']

    list_1, list_2 = zip(*sorted(zip(list_2, list_1)))

    print(list_1)
    print(list_2)


def test_doc():
    print(fm.navigator.__doc__)


def test_dic():
    dic = {"1": "a", 2: "b"}
    print(dic["1"])
    print(dic[2])


def test_copy():
    pic = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\qm_logo.psd"
    print("Sourse: %s" % pic)
    newname = input("Enter path: \n>> ")
    newname = newname if os.path.isabs(newname) else os.path.join(os.path.split(pic)[0], newname if newname.count('.') > 0 else newname + '.' + pic.split('.')[-1])
    input(newname)

    with open(pic, "rb") as fin:
        image = fin.read()

    with open(newname,"wb") as fout:
        fout.write(image)


# path = "F:\Work\CODE\Projects\SortManager\Sorted\Code F"
# print([path])
# print([path.strip()])
print(1), print(2) if True else None
