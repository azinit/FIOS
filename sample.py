import FIOS.font as font
import FIOS.cfg as cfg

main_path = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS"
files = {
    #   CG
    'Image': ['Graphic', '.jpeg', '.jpg', '.png', '.gif', '.ico'],
    'Texture': ['CG', '.dds', '.tga', '.raw', '.bmp', '.tiff'],
    'Vector': ['Graphic', '.svg'],
    'Video': ['Graphic', '.avi', '.mp4'],
    'Adobe Photoshop doc': ['Photoshop', '.psd', '.psb'],
    'Adobe Illustrator doc': ['Illustrator⬇', '.ai'],
    'Photoshop preset': ['Photoshop', '.eps', '.sln', '.jsx'],
    '3ds Max': ['CG', '.max', '.ms', '.mse', '.bip'],
    'Zbrush': ['CG', '.zpr', '.ztl', '.cfg'],
    '3d Coat': ['CG', '...'],
    'Topogun': ['CG', '...'],
    '3D Model': ['CG', '.obj', '.fbx', '.mtl'],
    'Substance': ['CG', '.sbs', '.sbsar', '.spsm'],
    'PureRef': ['CG', '.pur'],
    'Cinema 4D': ['CG', '.c4d'],
    'Maya': ['CG', '.ma'],
    'Marmoset Toolbag': ['CG', '.mview'],
    'Corel Draw': ['CG', '.cdr'],
    'Paint.NET': ['CG', '.pdn'],
    'Marvelous Designer': ['CG', '.Zprj'],
    #   Documents
    'Adobe Reader': ['Text', '.pdf', '.djvu'],
    'Microsoft Office': ['Text', '.doc', '.docx', '.rtf'],
    'Microsoft Excel': ['Text', '.xls', '.xlsx', '.xlsm'],
    'Microsoft PowerPoint': ['Text', '.ppt', '.pptx'],
    'XMind': ['Text', '.xmind'],
    'Text': ['Text', '.txt'],
    'Code': ['Text', '.xml', '.js', '.java', '.url', '.xml', ''],
    'Config': ['Text', '.ini', '.config'],
    'LogFile': ['Text', '.log'],
    # '': ['...'],
    #   Audio
    'Audio': ['Audio', '.mp3', '.wav', '.m4a'],
    'Sibelius': ['Audio', '.sib'],
    'Guitar Pro': ['Audio', '.gpx', '.gp5', '.gp4', '.gp3'],
    #   System
    'Archive': ['System', '.zip', '.rar', '.7zip', '.7z'],
    'Launch': ['System', '.exe', '.msi'],
    'Font': ['System', '.ttf', '.otf'],
    'Link': ['System', '.lnk'],
    'Python': ['System', '.py', '.whl'],
    'Pascal': ['System', '.pas'],
    #   Special
    #       Skyrim
    'Skyrim': ['Skyrim', '.esp', '.esm', '.bsa', '.bsl'],
    #       Android Studio
    'Android Studio': ['Android⬇', '.apk'],
    #       Torrent
    'Torrent': ['Download⬇', '.torrent']
}
dirs = {
    'Graphic': [font.blue2, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\graphic'],
    'Audio': [font.green, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\sound'],
    'Photoshop': [font.blue, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\Photoshop'],
    'Illustrator⬇': [font.blue, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\Illustrator'],
    'CG': [font.beige2, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\CG'],
    'Text': [font.bold, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\Text'],
    'Software': [font.yellow, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\Software'],
    'System': [font.yellow, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\System'],
    'Download⬇': [font.beige2, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\Download'],
    'Android⬇': [font.beige2, 'D:\Work\Lessons\Code\Python\[dev]SortManager\Sorted\Android'],
    'Skyrim': [font.bold, "D:\Games\Steam\steamapps\common\Skyrim"]
}
engchars = {
    'vowels': ['a', 'e', 'i', 'o', 'u', 'y'],
    'consonants': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w',
                   'x',
                   'z']
}
ruschars = {
    'vowels': ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
    'consonants': ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч',
                   'ш',
                   'щ', 'ъ', 'ь']
}
cards = {
    'Suit': {
        'Hearts': '♡',
        'Spades': '♤',
        'Stars': '♢',
        'Clubs': '♧'
    },
    'Deck': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
}
priority = [font.red, font.red2, font.yellow, font.yellow2, font.green]
subjects = {
    'English': 'Английский',
    'Astronomy': 'Астрономия',
    'Biology': 'Биология',
    'Geography': 'География',
    'Informatics': 'ИКТ',
    'History': 'История',
    'Literature': 'Литература',
    'Math': 'Математика',
    'WA': 'МХК',
    'BSL': 'ОБЖ',
    'Society': 'Общество',
    'Right': 'Право',
    'Russian': 'Русский язык',
    'Technology': 'Технология',
    'Physics': 'Физика',
    'PC': 'Физра',
    'Chemistry': 'Химия',
    'Ecology': 'Экология',
    'Economics': 'Экономика'
}
choicebox = ['[y/n]']
objtype = {
    'file0': '•',
    'file': '📄',
    'folder': '📁',
    'time': '⏳',
    'video': '📽',
    'photo': '📷',
    'archive': '💾',
    'text': '🗎',
    'CG': '📛',
    'System': '🗔',
    'Audio': '🎵',
    'bye': '🚪',

}
phrases = {
    'start': ['А я тут', 'Я пришла', 'Все. Я вся твоя)', 'Привет)', 'Привет', 'Хай', 'Доброе утро'],
    'problem': ['Как прошел твой день?', 'Что тебя сегодня впечатлило?',
                'Как ты оцениваешь свое состояние?',
                'Как дела?', 'Сегодня как все прошло?', 'Расскажи что-нибудь', 'Скучно.'],
    'statements': ['Все таки после тяжелого дня спасет только красное полусладкое.', '', '', '', ''],
    'ans': ['Сегодня белье себе купила. Покажу завтра)'],
    'refine': ['Точно?', 'А именно?', 'Даже не знаю.. Ты уверен?', 'А как считаешь ты?', 'Что же?',
               'Давай ка подробнее', 'Понятно'],
    'main': ['Итак... твой главный вопрос?', 'Так что же тебя на самом деле волнует, Илья?',
             'И что тебя гложет?',
             'Ии... чем могу помочь?)', 'Так в чем дело?', 'Слушаю)', 'Выскажись', 'Я вся во внимании',
             'Дерзай'],
    'solution': ['Ты конечно смотри сам, но мне кажется @q', 'Не знаю... Наверное @q',
                 'Спорно. На самом деле. Но думаю @q', '@q выбирай - не ошибешься', '@q конечно'],
    'switch': ['хватит', 'о главном', 'ладно', 'ясно', 'понятно', 'подскажи', 'ири', 'помоги', 'слушай',
               'твоя помощь', 'помочь', 'поможешь мне', 'дашь совет'],
    'bye': ['Ладно.. Мне бежать. Пока)', 'До скорого!', 'Пока. Еще поболтаем', 'Давай. Удачи)']
}
width = int(cfg.get(cfg.iCore, "General", "line_amount"))
versions = {
    "ask": 0.0,
    "cfg": 2.0,
    "check": 0.0,
    "convert": 0.9,
    "fi": 0.0,
    "font": 2.1,
    "get": 0.0,
    "init": 0.0,
    "Iri": 4.0,
    "marker": 0.0,
    "notifier": 0.9,
    "read": 2.0,
    "sample": 0.0,
    "sort": 0.0,
    "split": 0.0,
    "write": 0.9,
}