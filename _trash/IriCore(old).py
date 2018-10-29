import os
import sys
import time

import init
import get
import convert
import cfg

def read_properties():
    path = os.getcwd()+'\profile.ini'
    print(path)
    cfg.create(path, 'profile')
    # general = cfg.get(path, 'General', 'fullname')
    # contacts = cfg.get(path, 'Contacts')
    return 'Props'


def obj_properties():
    properties = read_properties()
    print(properties)

def fill_profile():
    print('👩 Как я поняла, ты хочешь создать новую анкету по человеку.')
    time.sleep(1.5)
    print('👩 Что ж, придется потерпеть, ведь вопросов у меня много')
    time.sleep(1)
    b = input('👩 Ты готов?)')
    if b == 'y' or not b:
        print('👩 Хорошо. В таком случае начнем.')
        fullname = input('• Как зовут девушку?(ну или парня)')
        status = input('• Его(ее) положение(статус)')
        birthday = input('• Знаешь день рождения этого человека?')
        line = input('• Чем занимается?')
        geoposition = input('• Где живет?')
        home = input('• Где родился этот человек?')
        print('👩 Хорошо. Так-с и запишем)')
        time.sleep(1)
        print('👩 Теперь пройдемся по контактам.')
        phone = input('• Номер телефона?')
        vk = input('• Есть в контакте?')
        ask = input('• Аск имеется?')
        instagram = input('• Инстаграмом балуется?')
        print('👩 Итак-с, имеем:')
        print(fullname, status, birthday, line, geoposition, home, phone, vk, ask, instagram)
        print('👩 До скорого :)')

# obj_properties()
fill_profile()
path = 'D:\Work\FIRI\FIOS'
