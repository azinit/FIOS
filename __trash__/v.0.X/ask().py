class ask:
    @staticmethod
    def clean(dirpath, lst=''):
        string = os.path.split(dirpath)[1]
        print(
            '%sClean ' % (font.beige2 + Feebon.initials + font.end) + font.blue + sample.objtype['folder'] + string + font.end + ' ? %s' %
            sample.choicebox[0])
        b = input(Feebon.pinitials)
        if b == 'y':
            b = True
            if string == 'Sorted':
                fi.clean(b)
            elif lst:
                fi.clean(b, lst)
            else:
                fi.clean(b, dirpath)
        else:
            b = False
            return b

    def path():
        # path = get.obj(self).path
        # path = input('Enter your path: ')
        # if path == 'enough' or path == 'fin':
        #    return True
        # if not path:
        #    path = current
        a, b = fi.navigator(CURRENT)
        return a, b

    def chat(integ=1, pattern='', switch=False):
        global counter
        steps = ['problem', 'refine', 'main', 'solution', 'bye']
        if not switch:
            step = steps[counter % 2]
            counter += 1
        else:
            step = steps[get.obj(integ).content]
        quote = random.choice(sample.phrases[step])
        # quote = step
        if len(pattern):
            print('{}👩 Дай-ка подумать...{}'.format(font.beige, font.end))
            a, c, f = [], 0, 0
            while True:
                if f == 1:
                    # print(a)
                    break
                a.clear()
                while True:
                    if c == 1:
                        c = 0
                        break
                    b = random.choice(pattern)
                    if len(a) == 0:
                        a.append(b)
                    else:
                        for v in a:
                            if v == b:
                                continue
                            else:
                                a.clear()
                                c = 0
                                break
                        else:
                            a.append(b)
                            c += 1
                            # print(a)
                f += 1
            pattern = font.yellow + a[0] + font.end
            print(font.beige + Feebon.initials + quote.replace('@q', pattern) + font.end)
        else:
            print(font.beige + Feebon.initials + quote + font.end)
    @staticmethod
    def attachment(path, listname):
        qu = 'Add %s for %s ? [y/n]: ' % (type, font.beige + listname + font.end)
        print()
        ask = input(qu)
        print()
        if ask == 'o':
            os.startfile(path)
            ask = input(qu)
            if ask == 'y':
                return True
            else:
                return False
        if ask == 'y':
            return True
        else:
            return False

    def main(self='empty', mode='clean', type='std', listname='std'):
        pass

    def start(text, choicebox=True, enter='', iri=True):
        if choicebox:
            box = sample.choicebox[0]
        else:
            box = ''
        color = iri * font.beige
        string = color + Feebon.initials + get.obj(str(text)).content + box + ' ' + font.end
        if enter:
            print(string)
            write.hms()
            b = input(enter)
        else:
            b = input(string)
        if b == 'y' or b == '':
            b = True
        else:
            b = False
        return b
