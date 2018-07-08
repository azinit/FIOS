import cfg
import os
import font
import time

main_path = os.getcwd() # + "\\" + "projects" + "\\" + "HS"
unis = ['КФУ', 'КГЭУ', 'КНИТУ-КАИ']
faculty = [['ИТИС', 'ИВМиИТ-ВМК'], ['ИЦТЭ'], ['ИКТиЗИ', 'ФМФ']]

print(os.listdir('F:\Work\FIOS\projects\HS\КНИТУ-КАИ'))
class S():
    tags_en = ['name', 'profile', 'description', 'sub', 'ave_score', 'min_score', 'plan']
    tags_ru = ['направление', 'профиль', 'описание', 'предметы', 'средний балл', 'минимальный балл', 'бюджетных мест']

class F():
    tags_en = ['name', 'description', 'directions', 'address', 'phone', 'ave_score', 'min_score', 'professions', 'scholarship', 'rating', 'reviews']
    tags_ru = ['полное название', 'описание', 'направлений обучения', 'адрес', 'контактный номер', 'средний балл', 'минимальный балл', 'профессии', 'стипендия', 'рейтинг', 'отзывы']


for i in range(len(unis)):
    folder = os.path.join(main_path, unis[i])
    for j in range(len(faculty[i])):
        file = os.path.join(folder, faculty[i][j] + '.ini')
        print(font.beige + font.bold + font.blackbg + 'Вуз: {}, Факультет: {}'.format(unis[i], faculty[i][j]) + font.end)
        time.sleep(0.5)
        try:
            k = 0
            for t in range(len(F.tags_en)):
                if t == 0:
                    prefix = '➢ '
                    color = font.beige + font.underline
                else:
                    prefix = '  • '
                    color = font.beige
                print('{}{}: {}'.format(prefix, F.tags_ru[t], color + cfg.get(file, str(k), F.tags_en[t])) + font.end)
            input('-' * 65)
        except:
            print('Error 0!!!')
        try:
            spec_amount = int(cfg.get(file, '0', 'directions'))
            if spec_amount > 0:
                for k in range(1, spec_amount + 1):
                    for t in range(len(S.tags_en)):
                        if t == 0:
                            prefix = '> '
                            color = font.beige + font.underline
                        elif t == 1:
                            color = font.beige
                            prefix = '  {}🏷{} '.format(font.bold, font.end)
                        elif t == 2:
                            color = font.beige
                            prefix = '  💼 '
                        elif t == 3:
                            color = font.beige
                            prefix = '  💻 '
                        elif t == 4:
                            color = font.blue2
                            prefix = '  🗃 '
                        elif t == 5:
                            color = font.red2
                            prefix = '  📑 '
                        elif t == 6:
                            color = font.yellow
                            prefix = '  📑 '
                        else:
                            prefix = '🎓'
                            color = font.beige

                        print('{}{}: {}'.format(prefix, S.tags_ru[t], color + cfg.get(file, str(k), S.tags_en[t])) + font.end)
                    if k == spec_amount:
                        input('> ...')
                        print()
                        print('=' * 65)
                    else:
                        input('-'*65)

        except:
            print('Error :(')

            # print(i, j)'''
    input('> Next university?')
    for h in range(13):
        print()


print('byebye, :)')
#  res = cfg.get("F:\Work\FIOS\projects\HS\КФУ\ИТИС.ini", '1', 'name')
# print(res)

