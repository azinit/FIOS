class fi:

    @staticmethod
    def create(filepath, b=None, public=True):
        # create folder
        # create directory
        # create file
        obj = init(filepath)
        path, kind, name = obj.path, obj.kind, obj.name
        try:
            if kind == 'Folder':
                if not os.path.exists(path):
                    name = os.path.split(path)[1]
                    os.chdir(os.path.split(path)[0])
                    os.mkdir(name)
                    b = True
                else:
                    b = False
            elif kind == 'File':
                cpath = [r"D:\Work\Lessons\Code\Python\[dev]CreateTheory", 'name.txt']
                # head, tail = split.file(name)
                if not os.path.exists(path) or b:
                    try:
                        os.chdir(cpath[0])
                        shutil.copy(cpath[1], os.path.split(path)[0])
                        os.chdir(os.path.split(path)[0])
                        os.rename(cpath[1], name)
                        # file = open(head+tail,'a')
                        # file = codecs.open(name,'a','utf-8')
                        # file.close()
                        # file = codecs.open(name,'r','utf-8')
                        # file.close()

                        b = True
                    except:
                        b = None
                        sys.exit(0)
                elif b != True:
                    b = False
            write.notification(path, b, access=public)
            return True
        except:
            e = sys.exc_info()[0]
            irila("{}: {}".format(e, path))
            return False

    @staticmethod
    def clean(path, listcontent=''):
        write.status()
        # clean directory
        # clean file content
        if listcontent == '':
            keys = list(map(lambda k: k*(k !='Skyrim'), sample.dirs.keys()))
            keys.remove('')
            array = list(map(lambda k: sample.dirs.get(k)[1], keys))
        else:
            array = listcontent
        if init(path).content:
            for f in array:
                for i in os.listdir(f):
                    try:
                        path = (os.path.join(f, i))
                        b = True
                        try:
                            # shutil.rmtree(path, ignore_errors=True)
                            pass
                        except:
                            # os.rmdir(path)
                            pass
                    except:
                        pass
                        b = False
                        # os.remove(path)
                write.notification(path, b, 'clean')
                # print('Directory ' + font.red + f + font.end + ' was cleaned.')

    @staticmethod
    def delete(path):
        for file in lst:
            if get(file).kind == 'Folder':
                shutil.rmtree(file, ignore_errors=True)
                print('Directory ' + font.red + file + font.end + ' was deleted.')
            elif get(file).kind == 'File':
                os.remove(file)
                print('File ' + font.red + file + font.end + ' was deleted.')
            else:
                print(Feebon.initials + 'Nothing to delete')
    def move(self, file, printmode=False):
        dst = get.obj(self).path
        s = ''
        if fi.create(dst, public=False):
            path = os.path.join(dst, file)
            try:
                shutil.move(file, dst)
                s += (font.blue + file + font.end)
            except:
                try:
                    file = check.duplicate(path, file)
                    shutil.move(file, dst)
                    s += (font.yellow + file + font.end)
                except:
                    e = sys.exc_info()[0]
                    irila("{}: {}".format(e, dst))
            if printmode:
                kind = get.obj(file).kind
                if kind == 'Folder':
                    symb = '📁'
                elif kind == 'File':
                    symb = '•'
                else:
                    symb = ''
                dst, s = split.path(dst), split.path(s)
                s = ('{0} {2} ➟ {1}📁 {4}{3} '.format(symb, font.beige, s, font.end, dst))
                # s = ('• {0} {2} ➟ {1}📁 {4}{3} '.format(FileType, DstColor, s, font.end, DstType))
                print(s)
        return s

    def open(self, printmode=False):
        path = get.obj(self).path
        file = split.path(path, 4)
        if printmode:
            print('Open: ' + font.green + file + font.end)
        os.startfile(path)

    def select(self):
        path = get.obj(self).path
        lst = os.listdir(path)
        write.status()
        if lst:
            write.printlist('select %s location' % (font.beige + 'next' + font.end), lst, 'iri')
            n, c = (input(font.beige + 'Next(or skip): ' + font.end)), len(lst)
            if n.isdigit():
                n = int(n)
                if n <= c:
                    file = lst[n - 1]
                    path = os.path.join(path, file)
                else:
                    n = 'refresh'
            elif isinstance(n, str):
                n = n.lower()
            # check input
            a, b = fi.input(n, path, 'selection')
            if not a:
                return (a, b)
            elif a:
                return (a, path)

    def navigator(self, pathname='next'):
        # =====================
        obj = get.obj(self)
        path, usd, exc = obj.path, marker.check(), marker.check(file=EXC_PATH)
        lst, rlst = [os.path.split(path)[0]] + os.listdir(path), [os.path.split(path)[0]] + os.listdir(path)
        # public
        write.status()
        print('Curdir: ' + font.beige + convert.tographpath(path) + font.end)
        # check used
        for count, i in enumerate(rlst):
            # input
            j, n, cont, ExtColor = os.path.join(path, i), '', '', ''
            # ext = '.' + split.file(get.obj(j).name)[1]
            # get dircontent
            if count != 0 and os.path.isdir(j):
                list1, list2 = (check.dircontent(j))
                if len(list2) == 1:
                    cont = list1
                else:
                    cont = write.priority(list1, list2, False)
                if cont:
                    cont = ' / ' + cont
            # check markers
            if (get.exceptions(j, exc)[1]) != None:
                n += font.red
            elif (get.exceptions(j, usd)[1]) != None:
                n += font.grey
            # check extension
            for filedir in sample.files.values():
                if (get.exceptions(j, filedir, mode='ext')[0]):
                    ExtColor = sample.dirs[filedir[0]][0]
                    break
            # check type
            if get.obj(j).kind == 'Folder':
                rlst[count] = n + '📁 ' + i + font.end + font.italic + cont
            elif get.obj(j).kind == 'File':
                rlst[count] = n + '• ' + ExtColor + i + font.end
        # file order
        order = sort.list.ieror(rlst)
        rlst, lst = [rlst[i] for i in order], [lst[i] for i in order]
        if rlst:
            write.printlist('select %s location' % (font.yellow + pathname + font.end), rlst, 'navigator')
            n, c = (input(font.yellow + 'Next(or skip): ' + font.end)), len(rlst) - 1
            if n.isdigit():
                n = int(n)
                if n <= c:
                    file = lst[n]
                    path = os.path.join(path, file)
                else:
                    n = 'refresh'
            elif isinstance(n, str):
                n = n.lower()
            # check input
            a, b = fi.input(n, path, 'navigator')
            if not a:
                return (a, b)
            elif a:
                if os.path.isdir(path):
                    path = fi.navigator(path, pathname)
                elif os.path.isabs(path):
                    print('Open: ' + font.green + file + font.end)
                    os.startfile(path)
                    path = fi.navigator(os.path.split(path)[0], pathname)
                else:
                    print('Error: ', path)
        return path

    def input(self, path=MPATH, process='test', mode='std'):
        name, sd = get.obj(self).content, ''
        if isinstance(name, str):
            nlst = name.split()
            # if have parameters
            if len(nlst) > 1:
                # set array
                nlst.remove(nlst[0])
                if len(nlst[0].split('-')) > 1:
                    d = convert.fromgap(nlst[0])
                    sd = nlst[0]
                else:
                    d = nlst
                    sb = ' '
                    sd = sb.join(d)
        funcdict = {
            'help': 'Get help for FiInput',
            'COMMON': '|',
            'type': 'Get type of {selected} folder',
            'ref': 'Refresh Directory Content',
            'sb': 'Get Subs of Current Directory',
            'sf': 'Get Files of Current Directory',
            'open': 'Open Current Directory',
            'exc': 'Set Extension Directory',
            'fin': 'Finish program',
            'clean': 'Clean from empty dirs',
            '/cancel': 'Cancel last operation',
            'del': 'Delete {selected}',
            '/sftype': 'Sort by filetype',
            'SPECIAL': '|',
            'rec': 'Start recursive action',
            'st': 'Choose step',
            'move': 'Move {source} to Selected Path {destination}',
        }
        if mode == 'std':
            if name == '':
                if process == 'navigator':
                    print('Selected: ' + font.beige + font.underline + path + font.end)
                    # print(font.violet + '%s finished' % (process.capitalize()) + font.end)
                else:
                    print(font.beige2 + '%s finished' % (process.capitalize() + font.end))
                return (False, 'Non' + path)
            if name == 'ref':
                return (False, 'ref' + path)
            elif name == 'sb':
                list(get.subs(path, printmode=True))
                # path = fi.navigator(path)
                return (False, 'sub' + path)
            elif name == 'sf':
                list(get.subs(path, True, True, printmode=True))
                # path = fi.navigator(path)
                return (False, 'sub' + path)
                # return (False, 'up' + path)
            elif name == 'up':
                print(font.violet + '__Navigator__' + font.end)
                parent, child = os.path.split(path)
                path = fi.navigator(parent)
                return (False, ('up' + path))
            elif name == 'st':
                return (False, ('step' + path))
            elif name == 'open':
                print('Open: {0}'.format(font.beige + path + font.end))
                os.startfile(path)
                input()
                return (False, 'opn' + path)
            elif name == 'fin':
                return (False, 'fin')
            elif name == 'clean':
                pass
            elif name == 'cancel':
                pass
                # npath = fi.navigator(path)
                # return (False, 'cnl'+ npath)
            elif name == 'rec':
                return (False, 'rec' + path)
            elif name == 'exc':
                return (False, 'exc' + path)
            elif name == 'move {0}'.format(sd):
                # source
                spath = get.file(path, d)
                print('{0}Source{1}: '.format(font.yellow + font.bold, font.end))
                print('• ', end='')
                print('\n• '.join(str(p) for p in spath))

                # counting
                count = 0
                for f in spath:
                    if get.obj(f).kind == 'Folder':
                        files = list(get.subs(f, False, True))[0]
                        count += len(files)
                    else:
                        files = spath.copy()
                        count += len(files)
                # choose destination
                intersection = check.intersection(spath)
                assign = True
                for theme in intersection:
                    DstColor = sample.dirs[theme][0]
                    DstType = sample.objtype['folder'] + ' '
                    text = (
                        'Is {}{}{} the {}destination?{}'.format(DstColor + font.bold, DstType, theme + font.end,
                                                                font.bold,
                                                                font.end))
                    b = ask.start(text, iri=False)
                    if b:
                        dpath = os.path.join(sample.dirs[theme][1], '[Sorted]')
                    else:
                        assign = False
                if not assign:
                    dpath = fi.navigator(SORTPATH, font.bold + 'destination')[1].split('Non')[1]
                    if os.path.split(dpath)[1] != '[Sorted]':
                        dpath = os.path.join(dpath, '[Sorted]')
                # move object
                for f in spath:
                    fi.move(dpath, f, True)
                input()
                return (False, 'mov' + str(count))
            elif name == 'del {0}'.format(sd):
                # source
                spath = get.file(path, d)
                print('{0}Selected{1}: '.format(font.red + font.bold, font.end))
                print('• ', end='')
                print('\n• '.join(str(p) for p in spath))
                fi.clean(True, lst=spath, mode='delete')
                input()
                return (False, 'del')
            elif name == 'help':
                write.printdict(name, funcdict)
                input()
                return (False, 'hlp' + path)
            elif name == 'type {0}'.format(sd):
                spath = get.file(path, d)
                print(check.intersection(spath))
                return (False, 'typ' + path)
            elif name or name == 0:
                return (True, 'None')
