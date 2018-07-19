import datetime

import FIOS.font as font

MAIN_PATH = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS"
#   File System
files = {
    #   CG
    "Image": [".jpeg", ".jpg", ".png", ".gif", ".ico"],
    "Texture": [".dds", ".tga", ".raw", ".bmp", ".tiff"],
    "Vector": [".svg"],
    "Video": [".avi", ".mp4"],
    "Adobe Photoshop doc": [".psd", ".psb"],
    "Adobe Illustrator doc": [".ai"],
    "Photoshop preset": [".eps", ".sln", ".jsx"],
    "3ds Max": [".max", ".ms", ".mse", ".bip"],
    "Zbrush": [".zpr", ".ztl", ".cfg"],
    "3d Coat": ["..."],
    "Topogun": ["..."],
    "3D Model": [".obj", ".fbx", ".mtl"],
    "Substance": [".sbs", ".sbsar", ".spsm"],
    "PureRef": [".pur"],
    "Cinema 4D": [".c4d"],
    "Maya": [".ma"],
    "Marmoset Toolbag": [".mview"],
    "Corel Draw": [".cdr"],
    "Paint.NET": [".pdn"],
    "Marvelous Designer": [".Zprj"],
    #   Documents
    "Adobe Reader": [".pdf", ".djvu"],
    "Microsoft Office": [".doc", ".docx", ".rtf"],
    "Microsoft Excel": [".xls", ".xlsx", ".xlsm"],
    "Microsoft PowerPoint": [".ppt", ".pptx"],
    "XMind": [".xmind"],
    "Text": [".txt"],
    "Code": [".xml", ".js", ".java", ".url", ".xml", ""],
    "Config": [".ini", ".config"],
    "LogFile": [".log"],
    # "": ["..."],
    #   Audio
    "Audio": [".mp3", ".wav", ".m4a"],
    "Sibelius": [".sib"],
    "Guitar Pro": [".gpx", ".gp5", ".gp4", ".gp3"],
    #   System
    "Archive": [".zip", ".rar", ".7zip", ".7z"],
    "Launch": [".exe", ".msi", ".bat"],
    "Font": [".ttf", ".otf"],
    "Link": [".lnk"],
    #   Code
    "Python": [".py", ".whl"],
    "Pascal": [".pas"],
    "Visual Studio": [".sln", ".cs", ".csproj"],
    "Android Studio": [".apk"],
    "UI Style": [".ui"],
    #   Special
    #       Games
    "Skyrim": [".esp", ".esm", ".bsa", ".bsl"],
    #       Torrent
    "Torrent": [".torrent"]
}
objects = {
    "substance": ">",
    "number": '🔢',
    "dataStructure": '📚',
    "string": '🙱',
    "flag": '🚩',
    "timeData": '⏳',
    "path": '🖇',
    "file": '📄',
    "folder": '📁',
    "element": '•',
    "video": '🎬',
    "slides": '🎟',
    "image": '🖻',
    "camera": '📷',
    "archive": '💾',
    "game": "🎮",
    "CG": '📛',
    "system": '🗔',
    "audio": '🎵',
    "guitar": '🎸',
    "piano": '🎹',
    "arrow": '➟',
    "net": '🖧',
    "cloth": '👗',
    "log": '📜',
    "draw": '🎨',
    "texture": '🌀',
    "font": '🗛',
    "vector": '❐',
    "play": '▶',
    "map": '📊',
    "settings": '🔧',
    "text": '📝',
    "table": '📅',
    "phone": '📱',
    "castle": '🏰',
    "house": '🕋',
    "code": '💻',
    "clip": '🔗',
    "people": '👥',
    "link": '⮬',
    "windows": '🗗',
    "grid": '▤',
    "bye": '🚪',

}
files_properties = {
    "Image": ["Graphic", objects.get("image")],
    "Texture": ["CG", objects.get("texture")],
    "Vector": ["Graphic", objects.get("vector")],
    "Video": ["Graphic", objects.get("video")],
    "Adobe Photoshop doc": ["Adobe", objects.get("camera")],
    "Adobe Illustrator doc": ["Adobe", objects.get("draw")],
    "Photoshop preset": ["Adobe", objects.get("settings")],
    "3ds Max": ["CG", objects.get("house")],
    "Zbrush": ["CG", objects.get("people")],
    "3d Coat": ["CG", objects.get("house")],
    "Topogun": ["CG", objects.get("house")],
    "3D Model": ["CG", objects.get("house")],
    "Substance": ["CG", objects.get("texture")],
    "PureRef": ["CG", objects.get("image")],
    "Cinema 4D": ["CG", objects.get("house")],
    "Maya": ["CG", objects.get("house")],
    "Marmoset Toolbag": ["CG", objects.get("camera")],
    "Corel Draw": ["CG", objects.get("draw")],
    "Paint.NET": ["CG", objects.get("draw")],
    "Marvelous Designer": ["CG", objects.get("cloth")],
    #   Documents
    "Adobe Reader": ["Text", objects.get("slides")],
    "Microsoft Office": ["Text", objects.get("text")],
    "Microsoft Excel": ["Text", objects.get("table")],
    "Microsoft PowerPoint": ["Text", objects.get("slides")],
    "XMind": ["Text", objects.get("map")],
    "Text": ["Text", objects.get("text")],
    "Code": ["Text", objects.get("code")],
    "Config": ["Text", objects.get("log")],
    "LogFile": ["Text", objects.get("log")],
    # "": ["..."],
    #   Audio
    "Audio": ["Audio", objects.get("audio")],
    "Sibelius": ["Audio", objects.get("piano")],
    "Guitar Pro": ["Audio", objects.get("guitar")],
    #   System
    "Archive": ["System", objects.get("archive")],
    "Launch": ["Software", objects.get("play")],
    "Font": ["System", objects.get("font")],
    "Link": ["System", objects.get("link")],
    #   Code
    "Python": ["Code", objects.get("code")],
    "Pascal": ["Code", objects.get("code")],
    "Visual Studio": ["Code", objects.get("windows")],
    "Android Studio": ["Code", objects.get("phone")],
    "UI Style": ["System", objects.get("grid")],
    #   Special
    #       Games
    "Skyrim": ["Games", objects.get("game")],
    #       Torrent
    "Torrent": ["Download⬇", objects.get("net")],
}
dirs = {
    "Audio": [font.green, "F:\Work\CODE\Projects\SortManager\Sorted\Audio"],
    "Adobe": [font.blue, "F:\Work\CODE\Projects\SortManager\Sorted\Adobe"],
    "Graphic": [font.blue2, "F:\Work\CODE\Projects\SortManager\Sorted\Graphic"],
    "CG": [font.beige2, "F:\Work\CODE\Projects\SortManager\Sorted\CG"],
    "Text": [font.bold, "F:\Work\CODE\Projects\SortManager\Sorted\Text"],
    "Software": [font.yellow, "F:\Work\CODE\Projects\SortManager\Sorted\Software"],
    "System": [font.yellow, "F:\Work\CODE\Projects\SortManager\Sorted\System"],
    "Download⬇": [font.beige2, "F:\Work\CODE\Projects\SortManager\Sorted\Download"],
    "Code": [font.beige2, "F:\Work\CODE\Projects\SortManager\Sorted\Code"],
    "Games": [font.bold, "F:\Work\CODE\Projects\SortManager\Sorted\Games"]
}

priority = [font.red2, font.red, font.yellow2, font.yellow, font.green]
choicebox = ["[y/n]"]
phrases = {
    "start": ["А я тут", "Я пришла", "Все. Я вся твоя)", "Привет)", "Привет", "Хай", "Доброе утро"],
    "problem": ["Как прошел твой день?", "Что тебя сегодня впечатлило?",
                "Как ты оцениваешь свое состояние?",
                "Как дела?", "Сегодня как все прошло?", "Расскажи что-нибудь", "Скучно."],
    "statements": ["Все таки после тяжелого дня спасет только красное полусладкое.", "", "", "", ""],
    "ans": ["Сегодня белье себе купила. Покажу завтра)"],
    "refine": ["Точно?", "А именно?", "Даже не знаю.. Ты уверен?", "А как считаешь ты?", "Что же?",
               "Давай ка подробнее", "Понятно"],
    "main": ["Итак... твой главный вопрос?", "Так что же тебя на самом деле волнует, Илья?",
             "И что тебя гложет?",
             "Ии... чем могу помочь?)", "Так в чем дело?", "Слушаю)", "Выскажись", "Я вся во внимании",
             "Дерзай"],
    "solution": ["Ты конечно смотри сам, но мне кажется @q", "Не знаю... Наверное @q",
                 "Спорно. На самом деле. Но думаю @q", "@q выбирай - не ошибешься", "@q конечно"],
    "switch": ["хватит", "о главном", "ладно", "ясно", "понятно", "подскажи", "ири", "помоги", "слушай",
               "твоя помощь", "помочь", "поможешь мне", "дашь совет"],
    "bye": ["Ладно.. Мне бежать. Пока)", "До скорого!", "Пока. Еще поболтаем", "Давай. Удачи)"]
}
types = {
    "number_int_pos": 128,
    "number_int_neg": -32,
    "number_float_pos": 35.5,
    "number_float_neg": -13.8,
    "number_complex": 1+1j,
    "dataStructure_list": [1, 1, 2, 3, 5],
    "dataStructure_*_matrix": [[0, 1, 2], [3, 4, 5]],
    "dataStructure_tuple": tuple([1, 1, 2, 3, 5]),
    "dataStructure_dictionary": {"1": "a", "2": "b"},
    "dataStructure_set": {1, 1, 2, 3, 5},
    "dataStructure_frozenset": frozenset({1, 1, 2, 3, 5}),
    "string_char": 'a',
    "string_line": "Process finished with exit code 0",
    "string_text": "[General]\ncorename = Iri",
    "flag_bool_true": True,
    "flag_bool_false": False,
    "flag_NoneType": None,
    "timeData_date": datetime.date.today(),
    "timeData_time": datetime.datetime.time(datetime.datetime.now()),
    "timeData_datetime": datetime.datetime.now(),
    "path_file_is": r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\sample.py",
    "path_dir_is": r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS",
    "path_file_isn't": r"Z:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\sample.py",
    "path_ambiguous": r"Z:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS",
    "path_file_ui": r"F:\Work\CODE\toStudy\Python\PyQt\Poems.ui",
    "path_file_launch": r"F:\Work\CODE\toStudy\Python\PyQt\converter.bat",
    "path_dir_sort": "F:\Work\CODE\Projects\SortManager\Sorted\Audio",
}
versions = {
    "requester": 0.0,
    "cfg": 2.0,
    "check": 0.0,
    "convert": 0.99,
    "fm": 0.8,
    # TODO
    "font": 2.19,
    "get": 0.99,
    "substance": 2.1,
    "index": 0.9,
    "iri": 4.0,
    "notifier": 0.99,
    "read": 2.0,
    "sample": 1.0,
    "sort": 0.9,
    "split": 0.99,
    "write": 0.9,
}

#   Special Symbols
engchars = {
    "vowels": ['a', 'e', 'i', 'o', 'u', 'y'],
    "consonants": ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
}
ruschars = {
    "vowels": ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
    "consonants": ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш',
                   'щ', 'ъ', 'ь']
}
cards = {
    "Suit": {
        "Hearts": '♡',
        "Spades": '♤',
        "Stars": '♢',
        "Clubs": '♧',
    },
    "Deck": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
}

#   MISC
subjects = {
    "English": "Английский",
    "Astronomy": "Астрономия",
    "Biology": "Биология",
    "Geography": "География",
    "Informatics": "ИКТ",
    "History": "История",
    "Literature": "Литература",
    "Math": "Математика",
    "WA": "МХК",
    "BSL": "ОБЖ",
    "Society": "Общество",
    "Right": "Право",
    "Russian": "Русский язык",
    "Technology": "Технология",
    "Physics": "Физика",
    "PC": "Физра",
    "Chemistry": "Химия",
    "Ecology": "Экология",
    "Economics": "Экономика"
}

if __name__ == "__main__":
    dicts = [files, objects, files_properties, dirs, phrases, versions, types, engchars, ruschars, cards, subjects]
    names = ["files", "objects", "files_properties", "dirs", "phrases", "versions", "types", "engchars", "ruschars",
             "cards", "subjects"]
    for i in range(len(dicts)):
        print('.'*13 + names[i].upper() + '.'*13)
        for key, value in dicts[i].items():
            print("{}: {}".format(key, font.paint(value)))
        print()
