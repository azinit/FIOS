import os
import re

import get


'''def fileorder(self, numlist=[]):
    list = os.listdir(get.obj(self).path)
    newlist = []
    if not numlist:
        numlist = [x for x in range(0,len(list)+1)]
    numlist.sort()
    for i in numlist:
        for j in list:
            num = re.findall(r'\d+',j)
            if num:
                if i == int(num[0]):
                    newlist.append(j)
    return newlist'''
def by_num(value):
    nums = list(map(lambda x: int(re.findall(r'\d+', x)[0]), value))
    print(value, nums)

def files_by_num(path, dirlist):
    if dirlist:
        nums = re.findall(r'\d+', dirlist[0])
        print(nums)
    else:
        return files_by_num(path, os.listdir(path))


path_ = r'D:\Work\Lessons\Code\Iri\[dev]CreateTheory\vs 1.0\test'
sub = 'definition_1.txt'
sub1 = 'definition1.txt'
sub2 = 'defini1tion1.txt'
# print(by_num(sub))
# print(by_num(sub1))
# print(by_num(sub2))
print(by_num(os.listdir(path_)))
# print(os.listdir(path_,))
'''def ieror(self, markered = 'sorted'):
    content = get.obj(self).content
    if markered != 'sorted':
        path = markered
        for count, i in enumerate(content):
            j = os.path.join(path, i)
            if get.obj(j).kind == 'Folder':
                content[count] = '📁 ' + i
            elif get.obj(j).kind == 'File':
                content[count] = '• ' + i
        # print(content)
    clist = ['📁','•']
    ielist = []
    if isinstance(content,list):
        glist = content
    elif os.path.isabs(content):
        glist = os.listdir(content)
    else:
        glist = []
    for c in clist:
        for i,f in enumerate(glist):
            if get.exceptions(f,c,fullmode= False)[0]:
                ielist.append(i)
    return ielist
def bynum(self, num):
    list = get.obj(self).content
    newlist = []
    col = int(len(list) / num)
    for i in range(0,num):
        for j in range(0,col):
            newlist.append(list[i+j*num])
    return newlist'''