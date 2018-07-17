import datetime

import FIOS.font as font
import FIOS.cfg as cfg

main_path = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS"

#   File System
files = {
    #   CG
    "Image": ["Graphic", ".jpeg", ".jpg", ".png", ".gif", ".ico"],
    "Texture": ["CG", ".dds", ".tga", ".raw", ".bmp", ".tiff"],
    "Vector": ["Graphic", ".svg"],
    "Video": ["Graphic", ".avi", ".mp4"],
    "Adobe Photoshop doc": ["Adobe", ".psd", ".psb"],
    "Adobe Illustrator doc": ["Adobe", ".ai"],
    "Photoshop preset": ["Adobe", ".eps", ".sln", ".jsx"],
    "3ds Max": ["CG", ".max", ".ms", ".mse", ".bip"],
    "Zbrush": ["CG", ".zpr", ".ztl", ".cfg"],
    "3d Coat": ["CG", "..."],
    "Topogun": ["CG", "..."],
    "3D Model": ["CG", ".obj", ".fbx", ".mtl"],
    "Substance": ["CG", ".sbs", ".sbsar", ".spsm"],
    "PureRef": ["CG", ".pur"],
    "Cinema 4D": ["CG", ".c4d"],
    "Maya": ["CG", ".ma"],
    "Marmoset Toolbag": ["CG", ".mview"],
    "Corel Draw": ["CG", ".cdr"],
    "Paint.NET": ["CG", ".pdn"],
    "Marvelous Designer": ["CG", ".Zprj"],
    #   Documents
    "Adobe Reader": ["Text", ".pdf", ".djvu"],
    "Microsoft Office": ["Text", ".doc", ".docx", ".rtf"],
    "Microsoft Excel": ["Text", ".xls", ".xlsx", ".xlsm"],
    "Microsoft PowerPoint": ["Text", ".ppt", ".pptx"],
    "XMind": ["Text", ".xmind"],
    "Text": ["Text", ".txt"],
    "Code": ["Text", ".xml", ".js", ".java", ".url", ".xml", ""],
    "Config": ["Text", ".ini", ".config"],
    "LogFile": ["Text", ".log"],
    # "": ["..."],
    #   Audio
    "Audio": ["Audio", ".mp3", ".wav", ".m4a"],
    "Sibelius": ["Audio", ".sib"],
    "Guitar Pro": ["Audio", ".gpx", ".gp5", ".gp4", ".gp3"],
    #   System
    "Archive": ["System", ".zip", ".rar", ".7zip", ".7z"],
    "Launch": ["Software", ".exe", ".msi"],
    "Font": ["System", ".ttf", ".otf"],
    "Link": ["System", ".lnk"],
    #   Code
    "Python": ["Code", ".py", ".whl"],
    "Pascal": ["Code", ".pas"],
    "Visual Studio": ["Code", ".sln", ".cs", ".csproj"],
    "Android Studio": ["Code", ".apk"],
    #   Special
    #       Games
    "Skyrim": ["Games", ".esp", ".esm", ".bsa", ".bsl"],
    #       Torrent
    "Torrent": ["Download⬇", ".torrent"]
}
dirs = {
    "Graphic": [font.blue2, "F:\Work\CODE\Projects\SortManager\Sort\Graphic"],
    "Audio": [font.green, "F:\Work\CODE\Projects\SortManager\Sort\Audio"],
    "Adobe": [font.blue, "F:\Work\CODE\Projects\SortManager\Sort\Adobe"],
    "CG": [font.beige2, "F:\Work\CODE\Projects\SortManager\Sort\CG"],
    "Text": [font.bold, "F:\Work\CODE\Projects\SortManager\Sort\Text"],
    "Software": [font.yellow, "F:\Work\CODE\Projects\SortManager\Sort\Software"],
    "System": [font.yellow, "F:\Work\CODE\Projects\SortManager\Sort\System"],
    "Download⬇": [font.beige2, "F:\Work\CODE\Projects\SortManager\Sort\Download"],
    "Code": [font.beige2, "F:\Work\CODE\Projects\SortManager\Sort\Code"],
    "Games": [font.bold, "F:\Work\CODE\Projects\SortManager\Sort\Games"]
}

#   FIOS
assistant = cfg.get(cfg.iCore, "General", "assistant")
assistant_full = cfg.get(cfg.iCore, "General", "assist_transcript")
user = cfg.get(cfg.iCore, "General", "user")
width = int(cfg.get(cfg.iCore, "General", "line_amount"))
priority = [font.red2, font.red, font.yellow2, font.yellow, font.green]
objects = {
    "file0": '•',
    "file": '📄',
    "folder": '📁',
    "time": '⏳',
    "video": '📽',
    "photo": '📷',
    "archive": '💾',
    "text": '🗎',
    "CG": '📛',
    "System": '🗔',
    "Audio": '🎵',
    "bye": '🚪',

}
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
    "dateStructure_*_matrix": [[0, 1, 2], [3, 4, 5]],
    "dataStructure_tuple": tuple([1, 1, 2, 3, 5]),
    "dataStructure_dictionary": {"1": "a", "2": "b"},
    "dataStructure_set": {1, 1, 2, 3, 5},
    "dataStructure_frozenset": frozenset({1, 1, 2, 3, 5}),
    "string_char": 'a',
    "string_line": "Process finished with exit code 0",
    "string_text": "[General]\ncorename = Iri",
    "boolean": True,
    "datetime_date": datetime.date.today(),
    "datetime_time": datetime.datetime.time(datetime.datetime.now()),
    "datetime_datetime": datetime.datetime.now(),
    "path_file_is": r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\sample.py",
    "path_dir_is": r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS",
    "path_file_isn't": r"Z:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\sample.py",
    "path_dir_isn't": r"Z:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS",
}
versions = {
    "ask": 0.0,
    "cfg": 2.0,
    "check": 0.0,
    "convert": 0.99,
    "fi": 0.0,
    # TODO
    "font": 2.19,
    "get": 0.99,
    "substance": 2.0,
    "index": 0.0,
    "iri": 4.0,
    "notifier": 0.99,
    "read": 2.0,
    "sample": 1.0,
    "sort": 0.0,
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
