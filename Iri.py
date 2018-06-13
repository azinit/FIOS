import font
# from FB.iConfig import *
# from datetime import datetime, time, date
# from decimal import Decimal
# import math
# import shutil
# import configparser
# import random
# import os
# import codecs
# import inspect
# import time
# import sys
# import re
# import traceback

#   Iri - SmartSystem with useful functions!
#   Besides, Iri's very polite, benevolent and soft
#   (especially for your mistakes :) )
#
#   version 3.0

#   NTD:
#   def time : I wait :(
#   def help
#   def IriDebug
#   split by module
#   define icon for file
#   merge by columns
# ============================= VARIABLES ==============================
# TESTPHRASE = 'Hello, I\'m Iri :)'
# MPATH = r'D:\Work\Lessons\Code\Iri\[dev]CreateTheory'
# SORTPATH = 'D:\Work\Lessons\Code\Iri\[dev]SortManager\Sorted'
# # current = ('D:\Work\Lessons\Code\Python\[dev]SortManager' + r'\toSort')
# CURRENT = 'D:\DataBase\Sort'
# USED_PATH = r'D:\Work\Lessons\Code\Iri\FB\used.txt'
# EXC_PATH = r"D:\Work\Lessons\Code\Iri\FB\exc.txt"
# CFG_PATH = 'D:\Work\Lessons\Code\Iri\FB\Iri.ini'
# PROFILE_PATH = 'D:\Work\Lessons\Code\Iri\FB\profile.ini'

# CFG_FILE = cfg(CFG_PATH)
# PROFILE = cfg(PROFILE_PATH)
# counter = 0

# ============================== CLASSES ===============================


class Iri(object):

    def __init__(self, nickname = '', firstname = ''):
        self.MAINAME = CFG_FILE.get('General mainame')
        self.VERSION = CFG_FILE.get('General version')
        self.LINE = int(CFG_FILE.get('General line_amount'))

        self.MPATH = MPATH
        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        self.NICKNAME = text[:text.find('=')].strip()
        self.FIRSTNAME = PROFILE.get('%s firstname' % ('Feebon'))

        self.startime = 0
        self.mode = 'Info get'
        self.projectname = 'Test'
        self.pinitials = font.beige2 + '🗿 ' + font.end
        self.initials = '👩 '
        # self.erotic = font.violet2
        self.pos = font.blue
        self.neg = font.red2
    # TODO
    def developeme(self):
        item = inspect.stack()[1][3].upper()
        pass
    # TODO
    def user_info(self):
        pass
    def project_info(self, projectname = '', mode = '', talk = False):
        if not projectname:
            projectname = self.projectname
        else:
            self.projectname = projectname
        if not mode:
            mode = self.mode
        else:
            self.mode = mode

        print(font.beige + '%s interactive system | version: %s | font version: %s' % (self.MAINAME, self.VERSION, font.version) + font.end)
        now = datetime.now()
        print('Time: ' + font.beige + str(now) + font.end)
        print('Project: ' + font.beige + projectname + font.end)
        print('Hello, ' + font.blue + self.NICKNAME + font.end + '!')
        print("I'm " + font.beige2 + '%s :)' % self.MAINAME + font.end)
        if not talk:
            print("Let's " + font.yellow + self.mode + font.end + " something)")
        else:
            print("Давай {}поговорим.{}".format(font.yellow, font.end))
        write.status('main', '=')
        self.startime = int(now.hour) * 3600 + int(now.minute) * 60 + int(now.second)
        return
    def countime(self):
        now = datetime.now()
        endtime = int(now.hour) * 3600 + int(now.minute) * 60 + int(now.second)
        difference = abs(endtime - self.startime)
        difference = [str(divmod(difference, 3600)[0]), 'h:',
                      str(divmod(difference, 60)[0] - (divmod(difference, 3600)[0] * 60)), 'm:',
                      str(difference - (divmod(difference, 60)[0] * 60)), 's']
        count = ''
        for i in difference:
            count += i
        return count
    def byebye(self):
        write.status('=', '=')
        count = Iri.countime(self)
        process = check.verb(self.mode).capitalize()
        print(font.beige + process + ' finished!' + font.end)
        print(font.beige + 'In: ' + font.beige2 + count + font.end)
        print(font.beige + 'Your %s' % font.beige2 + self.MAINAME + font.end)
        print(font.blackbg + '© Mirilian Inc' + font.end)
    def update_version(self):
        newvers = (Decimal(self.VERSION) + Decimal(0.1)).quantize(Decimal('.0'))
        print(newvers)
        cfg.set(CFG_FILE, 'General version', str(newvers))
        write.status('Version Updated!')

Feebon = Iri()
# ======================================================================
class sort:
    pass

class marker:
    def def_file(self):
        file = get.obj(self).content
        if not file:
            us = USED_PATH
        else:
            us = file
        return us

    def new(self=MPATH, file=''):
        path = get.obj(self).path
        us = marker.def_file(file)
        # ==========================
        createf('temp', path)
        spath = os.path.join(path, 'temp')
        shutil.copy('name.txt', spath)
        os.chdir(spath)
        name = 'usedbase' + '.txt'
        os.rename('name.txt', name)
        print(font.yellow + name + font.end + ' created!')

    def append(self=MPATH, file=''):
        path = get.obj(self).path
        us = marker.def_file(file)
        # ==========================
        os.chdir(os.path.join(MPATH, 'temp'))
        with codecs.open(us, 'a', 'utf-8') as usedbase:
            usedbase.writelines(path)
            usedbase.writelines('\n')
            # print(font.grey + path + font.end + ' added as used!')

    def check(self=MPATH, file=''):
        path = get.obj(self).path
        us = marker.def_file(file)
        # ==========================
        used = []
        os.chdir(os.path.join(MPATH, 'temp'))
        with codecs.open(us, 'r+', 'utf-8') as usedbase:
            for lines in usedbase:
                lines = lines[:-1:]
                used.append(lines)
        # for u in used:
        #    print(font.ext.grey + u + font.ext.end + ' was used!')
        return used

    def clean(self=MPATH, file=''):
        path = get.obj(self).path
        us = marker.def_file(file)
        # ==========================
        os.chdir(os.path.join(MPATH, 'temp'))
        with codecs.open('usedbase.txt', 'w', 'utf-8') as usedbase:
            usedbase.write('')
            print(font.red + 'usedbase.txt' + font.end + ' cleaned!')

    def content(self, pattern):
        content = get.obj(self).content
        if isinstance(content, str):
            i = content.find(pattern)
            return i
        else:
            return None

    def string(line, color='std'):
        string = get.obj(line).string
        if color == 'std':
            string = font.red + string + font.end
        elif color == 'iri':
            string = font.beige2 + string + font.end
        return string
# ======================================================================
def irila(*args):
    if not args:
        text = 'I\'m Iri :)'
        print(Feebon.initials + font.beige2 + str(text) + font.end)
    else:
        print(Feebon.initials, end='')
        for text in args:
            print(font.beige2 + str(text) + font.end, end=' ')
        print()



    #newvers = (version + Decimal(0.1)).quantize(Decimal('.0'))
    # ===================================
    #config.set('General','version', str(newvers))
    #version = config.get('General', 'version')
    #print(mainame, version)
    #with open(path, "w") as config_file:
    #    config.write(config_file)
def randomize(self, amount, kit, it = 'none'):
    # write.public()
    printlst = []
    if it == 'none':
        it = (int(divmod(kit,amount)[0]))
    for j in range(0, it+1):
        lst = [x for x in range(1, kit + 1)]
        iteration = random.choice(lst)
        for i in range(1, iteration+1):
            random.shuffle(lst)
            lst.reverse()
        for a in range(0,amount):
            printlst.append(str(lst[a]))
    # check.digits(printlst)
    sep = (int((len(printlst) / amount)))
    s = ''
    c = 0
    # printlst = sort.list.bynum(printlst, amount)
    for i,p in enumerate(printlst):
        s += (font.beige2 + p + ' ' + font.end)
        if (i+1) % sep == 0:
            c += 1
            print('%s. %s' % (font.yellow + str(check.digits(c)) + font.end,s))
            s = ''
# ==============================================
# cfg.create(cfg_file)
# cfg_file.set('General line_amount',str(69))
# if __name__ == '__main__' or __name__ == 'init':
    # print(3)
    # get.iri(3)
    # get.info(3)
    # print(split.file('1408754.png.jpg'))
    # check.digits([0, 1, 2])
    # get.info(r"D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic\[Sorted]\1408754.png.jpg")
    # font.family()
    # font.color()
    # font.background()


# ==============================================