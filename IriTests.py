# from FB.IriM import *
# from FB.Iri import *
from FB.IriDev.Iri import *
import time
from datetime import datetime
import inspect
import os
import re
import tkinter.font as tk
# from tkinter import font
# ===================================================================
Feebon.project_info()
obj = {
    'file01': "D:\Games\Steam\steamapps\common\Skyrim\Data\Mirilian.esp",
    'file02': "D:\Games\Steam\steamapps\common\Skyrim\Data\Mirilian.esp.esp",
    'file03': r"D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic\[Sorted]\1408754.jpg",
    'file04': r"D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic\[Sorted]\1408754.png.jpg",
    'file05': r"D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic\[Sorted]\1408755.jpeg",
    'folder01': "D:\Work\Lessons\Code\Iri\FB",
    'folder02': "D:\Games\Steam\steamapps\common\Irina",
    'folder03': 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic\[Sorted',
    'folder04': "D:\Games\Steam\steamapps\common\Skyrim\Data",
    'folder05': r'D:\Work\Lessons\Code\Python\[dev]CreateTheory\vs 1.0\Planimetry\Circle\Arc\Formulas',
    'folder06': r'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic\11.11.17',
    'folder07': r'D:\DataBase\Sort\Models and other',
    'folder08': r'D:\DataBase\Sort\NewPr',
    'line': 'SGeneralMasterMismatchWarning=One or more plugins could not find the correct versions of the master files they depend on. Errors may occur during load or game play. Check the "Warnings.txt" file for more information.',
    'number': 123,
    'time00': datetime.now(),
    'time01': datetime.strptime('13:24:09','%H:%M:%S'),
    'time02': datetime.strptime('13:24:40','%H:%M:%S'),
    'date': '',
    'deprofile': '',
    'list': ['1','2','3'],
    'list01': [0, 0, 4, 0, 0],
    'list02': ['three', 'two', 'four', 'one', 'one2'],
    'Feebonacii list': [0, 1, 1, 2, 3, 5, 8],
    'password': '',
    'login': '',
    'verb': 'info get',
    'dictionary' : '',
    'filename': 'Screenshot13.bmp'
}

testdict = {
    '1': 5,
    '3': 3,
    '2': 4,
    '4': 2,
    '5': 1
}
dictionary = ['get', 'set', 'start', 'award', 'play', 'create', 'compare', 'share', 'invite', 'info get']
chlist = list(range(0, 16))
regular = '12) Text'
a = 1
b = 3
c = '!'
# time.sleep(1)
# ===================================================================
class Main(object):
    line = 69
    def __init__(self,content):
        # self.name = "'" + str(content) + "'"
        # self.path = "//" + str(content)
        self.content = content

    def info(self):
        obj = Main.obj(self)
        print(obj.content)

    def obj(self):
        self = Main(self)
        return self
class printe(Main):
    def pub(self):
        print(self.content*self.line)

def Yld(list):
    for i in list:
        yield i
# ===================================================================
# splitsybmol('x','-')
# Iri.irila(Feebon, obj['time'])
# print(re.findall(r'\w+', obj['filename']))
# print(re.findall(r'\w+\d+', obj['filename']))
# helv36 = tkinter.font.ITALIC('Hello')
# print(helv36)
# oldlist = ['1','2']
# print([oldlist])
# oldlist = list(map(int,oldlist))
# print([oldlist])
# string = re.findall('[A-Za-z]', regular)
# print(string)
# print(check.intersection([1,2,3,4,5], [1,1,2,3,5]))
# print((Yld(obj['list'])))
# ================================GET================================
# get.info(obj['Feebonacii list'])
# ✓ LAST print(get.lastnumber(obj,'.bmp',['']))
# ✓ EXCP sexc = (get.exceptions(c,['!','?']))[0]
# print(get.dirlevel(r'D:\Work'))
# print(get.dirinfo(obj['folder01']))
# ===============================CHECK================================
# ✓ DUPL print(check.duplicate(obj['file03']))
# ✓ NAME fpath = r'D:\Work\Lessons\Code\Python\[dev]SortManager\toSort\bkRpq4C.jx.c.jpg'
# ✓ NAME print(check.name(fpath))
# list1, list2 = (check.dircontent(r'D:\DataBase\Sort\textures&alpha'))
# write.priority(list1, list2)
# ✓ os.chdir(obj['folder04'])
# ✓ new, ext = 'Mirilian', '.esp'
# ✓ fullname = 'Mirilian.esp'
# ✓ os.rename(fullname, new + '(2)' + ext)
# ✓ print(fullname)
print(check.dircontent(obj['folder01']))
# get.dirinfo('D:\Games')
# get.info('D:\Games')
# ✓ VERB for word in dictionary:
# ✓ VERB    print(check.verb(word))
# ===============================SPLIT================================
# ✓ SPLT print(split.file('Screenshot.bmp'))
# print(split.file('jquery-1.10.2.min.js'))
# ================================RAND================================
# ✓ for i in range(0,3):
# ✓    randomize(Feebon, a,b)
# ================================SORT================================
# ✓ sort.list.fileorder(obj['folder05'])
# ✓ (sort.dict.value(testdict, True))
# D (sort.list.bynum(chlist, 1))
# ===============================WRITE================================
# ✓ PUBL write.public('TesTFunction')1
# write.tofile()
# ===============================CREATE===============================
# ✓ CRTE fi.create(obj['file05'])
# fi.navigator(obj['folder01'])
# ===============================CONVERT==============================
# path = r'D:\Work\Lessons\Code\Python\[dev]SortManager\toSort\SortPr\7'
# print(convert.tographpath(path))
# print(convert.fromgap('4-6'))
# ================================MAIN================================
# obj = Main(obj['list'])
# Main.path(obj)
# Main.info((obj['list']))
# print(obj.content)
# printe.pub(obj)
# ================================DICT================================
# for c in dict.priority:
#     print(c + 'Text' + font.end)
# ===============================CONFIG===============================
# ✓ create('D:\Work\Lessons\Code\Python\FB\Iri.ini')
# ✓ pars('D:\Work\Lessons\Code\Python\FB\Iri.ini')
# ===================================================================
Feebon.byebye()
