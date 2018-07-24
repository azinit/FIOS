import datetime

import FIOS.font as _f

# TODO: offset = 30
MAIN_PATH = r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS"
#   File System
files = {
    #   CG
    "Image":                    [".jpeg", ".jpg", ".png", ".gif", ".ico"],
    "Texture":                  [".dds", ".tga", ".raw", ".bmp", ".tiff"],
    "Vector":                   [".svg"],
    "Video":                    [".avi", ".mp4"],
    "Adobe Photoshop doc":      [".psd", ".psb"],
    "Adobe Illustrator doc":    [".ai"],
    "Photoshop preset":         [".eps", ".sln", ".jsx"],
    "3ds Max":                  [".max", ".ms", ".mse", ".bip"],
    "Zbrush":                   [".zpr", ".ztl", ".cfg"],
    "3d Coat":                  ["..."],
    "Topogun":                  ["..."],
    "3D Model":                 [".obj", ".fbx", ".mtl"],
    "Substance":                [".sbs", ".sbsar", ".spsm"],
    "PureRef":                  [".pur"],
    "Cinema 4D":                [".c4d"],
    "Maya":                     [".ma"],
    "Marmoset Toolbag":         [".mview"],
    "Corel Draw":               [".cdr"],
    "Paint.NET":                [".pdn"],
    "Marvelous Designer":       [".Zprj"],
    #   Documents
    "Adobe Reader":             [".pdf", ".djvu"],
    "Microsoft Office":         [".doc", ".docx", ".rtf"],
    "Microsoft Excel":          [".xls", ".xlsx", ".xlsm"],
    "Microsoft PowerPoint":     [".ppt", ".pptx"],
    "XMind":                    [".xmind"],
    "Text":                     [".txt"],
    "Code":                     [".xml", ".js", ".java", ".url", ".xml", ""],
    "Config":                   [".ini", ".config"],
    "LogFile":                  [".log"],
    # "": ["..."],
    #   Audio
    "Audio":                    [".mp3", ".wav", ".m4a"],
    "Sibelius":                 [".sib"],
    "Guitar Pro":               [".gpx", ".gp5", ".gp4", ".gp3"],
    #   System
    "Archive":                  [".zip", ".rar", ".7zip", ".7z"],
    "Launch":                   [".exe", ".msi", ".bat"],
    "Font":                     [".ttf", ".otf"],
    "Link":                     [".lnk"],
    #   Code
    "Python":                   [".py", ".whl", ".pyc"],
    "Pascal":                   [".pas"],
    "Visual Studio":            [".sln", ".cs", ".csproj"],
    "Android Studio":           [".apk"],
    "UI Style":                 [".ui"],
    "WEB":                      [".html", ".css", ".js"],
    #   Special
    #       Games
    "Skyrim":                   [".esp", ".esm", ".bsa", ".bsl"],
    #       Torrent
    "Torrent":                  [".torrent"]
}
objects = {
    "substance":                '>',
    "bin":                      '🗑',
    "number":                   '🔢',
    "sort":                     '🔁',
    "dataStructure":            '📚',
    "string":                   '🙱',
    "flag":                     '🚩',
    "timeData":                 '⏳',
    "path":                     '🖇',
    "file":                     '📄',
    "folder":                   '📁',
    "e_folder":                 '🗀',
    "d_folder":                 '📂',
    "element":                  '•',
    "video":                    '🎬',
    "slides":                   '🎟',
    "image":                    '🖻',
    "camera":                   '📷',
    "archive":                  '💾',
    "game":                     "🎮",
    "CG":                       '📛',
    "system":                   '🗔',
    "audio":                    '🎵',
    "guitar":                   '🎸',
    "piano":                    '🎹',
    "arrow_r":                  '🢤',
    "arrow":                    '➠',
    "arrow_broken":             '⭍',
    "net":                      '🖧',
    "cloth":                    '👗',
    "log":                      '📜',
    "draw":                     '🎨',
    "texture":                  '🌀',
    "font":                     '🗛',
    "vector":                   '❐',
    "play":                     '▶',
    "map":                      '📊',
    "settings":                 '🔧',
    "text":                     '📝',
    "table":                    '📅',
    "phone":                    '📱',
    "castle":                   '🏰',
    "house":                    '🕋',
    "code":                     '💻',
    "clip":                     '🔗',
    "people":                   '👥',
    "link":                     '⮬',
    "windows":                  '🗗',
    "grid":                     '▤',
    "bye":                      '🚪',
    "question":                 '❓',
    "vfx":                      '🎆',
    "dragon":                   '🐉',

}
files_properties = {
    "Image":                    ["Graphic", objects["image"]],
    "Texture":                  ["CG", objects["texture"]],
    "Vector":                   ["Graphic", objects["vector"]],
    "Video":                    ["Graphic", objects["video"]],
    "Adobe Photoshop doc":      ["Adobe", objects["camera"]],
    "Adobe Illustrator doc":    ["Adobe", objects["draw"]],
    "Photoshop preset":         ["Adobe", objects["settings"]],
    "3ds Max":                  ["CG", objects["house"]],
    "Zbrush":                   ["CG", objects["people"]],
    "3d Coat":                  ["CG", objects["house"]],
    "Topogun":                  ["CG", objects["house"]],
    "3D Model":                 ["CG", objects["house"]],
    "Substance":                ["CG", objects["texture"]],
    "PureRef":                  ["CG", objects["image"]],
    "Cinema 4D":                ["CG", objects["house"]],
    "Maya":                     ["CG", objects["house"]],
    "Marmoset Toolbag":         ["CG", objects["camera"]],
    "Corel Draw":               ["CG", objects["draw"]],
    "Paint.NET":                ["CG", objects["draw"]],
    "Marvelous Designer":       ["CG", objects["cloth"]],
    #   Documents
    "Adobe Reader":             ["Text", objects["slides"]],
    "Microsoft Office":         ["Text", objects["text"]],
    "Microsoft Excel":          ["Text", objects["table"]],
    "Microsoft PowerPoint":     ["Text", objects["slides"]],
    "XMind":                    ["Text", objects["map"]],
    "Text":                     ["Text", objects["text"]],
    "Code":                     ["Text", objects["code"]],
    "Config":                   ["Text", objects["log"]],
    "LogFile":                  ["Text", objects["log"]],
    # "": ["..."],
    #   Audio
    "Audio":                    ["Audio", objects["audio"]],
    "Sibelius":                 ["Audio", objects["piano"]],
    "Guitar Pro":               ["Audio", objects["guitar"]],
    #   System
    "Archive":                  ["System", objects["archive"]],
    "Launch":                   ["Software", objects["play"]],
    "Font":                     ["System", objects["font"]],
    "Link":                     ["System", objects["link"]],
    #   Code
    "Python":                   ["Code", objects["code"]],
    "Pascal":                   ["Code", objects["code"]],
    "Visual Studio":            ["Code", objects["windows"]],
    "Android Studio":           ["Code", objects["phone"]],
    "UI Style":                 ["System", objects["grid"]],
    "WEB":                      ["Code", objects["code"]],
    #   Special
    #       Games
    "Skyrim":                   ["Games", objects["game"]],
    #       Torrent
    "Torrent":                  ["Download⬇", objects["net"]],
}
dirs = {
    "Audio":        [_f.violet, "F:\Work\CODE\Projects\SortManager\Sorted\Audio", objects["audio"]],
    "Adobe":        [_f.beige, "F:\Work\CODE\Projects\SortManager\Sorted\Adobe", objects["camera"]],
    "Graphic":      [_f.blue2, "F:\Work\CODE\Projects\SortManager\Sorted\Graphic", objects["image"]],
    "CG":           [_f.beige, "F:\Work\CODE\Projects\SortManager\Sorted\CG", objects["draw"]],
    "Text":         [_f.white, "F:\Work\CODE\Projects\SortManager\Sorted\Text", objects["text"]],
    "Software":     [_f.yellow, "F:\Work\CODE\Projects\SortManager\Sorted\Software", objects["play"]],
    "System":       [_f.blackbg, "F:\Work\CODE\Projects\SortManager\Sorted\System", objects["system"]],
    "Download⬇":    [_f.beige2 + _f.bold, "F:\Work\CODE\Projects\SortManager\Sorted\Download", objects["net"]],
    "Code":         [_f.beige, "F:\Work\CODE\Projects\SortManager\Sorted\Code", objects["code"]],
    "Games":        [_f.red, "F:\Work\CODE\Projects\SortManager\Sorted\Games", objects["game"]],
    "Unassigned":   ['', r"F:\Work\CODE\Projects\SortManager\Sorted\Unassigned", objects["question"]]
}

priority = [_f.red2, _f.red, _f.yellow2, _f.yellow, _f.green]
choicebox = ["[y/n]"]
phrases = {
    "start":        ["А я тут", "Я пришла", "Все. Я вся твоя)", "Привет)", "Привет", "Хай", "Доброе утро"],
    "problem":      ["Как прошел твой день?", "Что тебя сегодня впечатлило?", "Как ты оцениваешь свое состояние?", "Как дела?", "Сегодня как все прошло?", "Расскажи что-нибудь", "Скучно."],
    "statements":   ["Все таки после тяжелого дня спасет только красное полусладкое.", "", "", "", ""],
    "ans":          ["Сегодня белье себе купила. Покажу завтра)"],
    "refine":       ["Точно?", "А именно?", "Даже не знаю.. Ты уверен?", "А как считаешь ты?", "Что же?", "Давай ка подробнее", "Понятно"],
    "main":         ["Итак... твой главный вопрос?", "Так что же тебя на самом деле волнует, Илья?", "И что тебя гложет?", "Ии... чем могу помочь?)", "Так в чем дело?", "Слушаю)", "Выскажись", "Я вся во внимании", "Дерзай"],
    "solution":     ["Ты конечно смотри сам, но мне кажется @q", "Не знаю... Наверное @q", "Спорно. На самом деле. Но думаю @q", "@q выбирай - не ошибешься", "@q конечно"],
    "switch":       ["хватит", "о главном", "ладно", "ясно", "понятно", "подскажи", "ири", "помоги", "слушай", "твоя помощь", "помочь", "поможешь мне", "дашь совет"],
    "bye":          ["Ладно.. Мне бежать. Пока)", "До скорого!", "Пока. Еще поболтаем", "Давай. Удачи)"]
}
types = {
    "number_int_pos":               128,
    "number_int_neg":               -32,
    "number_float_pos":             35.5,
    "number_float_neg":             -13.8,
    "number_complex":               1+1j,
    "dataStructure_list":           [1, 1, 2, 3, 5],
    "dataStructure_*_matrix":       [[0, 1, 2], [3, 4, 5]],
    "dataStructure_tuple":          tuple([1, 1, 2, 3, 5]),
    "dataStructure_dictionary":     {"1": "a", "2": "b"},
    "dataStructure_set":            {1, 1, 2, 3, 5},
    "dataStructure_frozenset":      frozenset({1, 1, 2, 3, 5}),
    "string_char":                  'a',
    "string_line":                  "Process finished with exit code 0",
    "string_text":                  "[General]\ncorename = Iri",
    "string_slash":                 '/',
    "string_double_slash":          "//",
    "string_multi_slash":           "////",
    "string_slash_":                '\\'[:1],
    "string_double_slash_":         "\\",
    "string_multi_slash_":          "\\\\",
    "flag_bool_true":               True,
    "flag_bool_false":              False,
    "flag_NoneType":                None,
    "timeData_date":                datetime.date.today(),
    "timeData_time":                datetime.datetime.time(datetime.datetime.now()),
    "timeData_datetime":            datetime.datetime.now(),
    "path_file_is":                 r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\sample.py",
    "path_dir_is":                  r"C:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS",
    "path_file_isn't":              r"Z:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS\sample.py",
    "path_ambiguous":               r"Z:\Users\Feebon\AppData\Local\Programs\Python\Python36-32\Lib\FIOS",
    "path_file_ui":                 r"F:\Work\CODE\toStudy\Python\PyQt\Poems.ui",
    "path_file_launch":             r"F:\Work\CODE\toStudy\Python\PyQt\converter.bat",
    "path_dir_sort":                r"F:\Work\CODE\Projects\SortManager\Sorted\Audio",
    "path_file_zbrush":             r"F:\Work\CODE\Projects\SortManager\Sorted\Unassigned\HelloWorld.ZTL",
    "path_file_exe":                r"F:\Work\CODE\Projects\SortManager\Sorted\Unassigned\kts18.0.0.405abcdefgru_13930.exe",
    "path_file_torrent":            r"F:\Work\CODE\Projects\SortManager\Sorted\Unassigned\Sony Vegas Pro 13.0 Build 453 Multilingual.torrent",
    "path_file_html":               r"F:\Work\CODE\Projects\SortManager\Sorted\Unassigned\messages_Даниил Герасимов(167539495).html",
    "path_file_unassigned":         r"F:\Work\CODE\Projects\SortManager\Sorted\Unassigned\messages_Даниил Герасимов(167539495).ttytp",
    "path_folder_deep":             r"F:\Work\CODE\toStudy",
    "path_folder_invalid":          r"F:\Work\CODE\Projects\SortManager\Sorted\Code ",
    "path_folder_invalid_":         r"F:\Work\CODE\toStudy\Python\my_second",
}
versions = {
    "requester":    1.0,
    "cfg":          2.0,
    "check":        0.0,
    "convert":      0.99,
    "fm":           1.0,
    "font":         2.19,   # TODO
    "get":          0.99,
    "substance":    2.2,
    "index":        0.9,
    "iri":          4.0,
    "notifier":     1.0,
    "read":         2.0,
    "sample":       1.1,
    "sort":         0.9,
    "split":        0.99,
    "write":        0.9,
}

#   Special Symbols
engchars = {
    "vowels":       ['a', 'e', 'i', 'o', 'u', 'y'],
    "consonants":   ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
}
ruschars = {
    "vowels":       ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'],
    "consonants":   ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь']
}
cards = {
    "Suit": {
        "Hearts":   '♡',
        "Spades":   '♤',
        "Stars":    '♢',
        "Clubs":    '♧',
    },
    "Deck": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
}

#   MISC
subjects = {
    "English":      "Английский",
    "Astronomy":    "Астрономия",
    "Biology":      "Биология",
    "Geography":    "География",
    "Informatics":  "ИКТ",
    "History":      "История",
    "Literature":   "Литература",
    "Math":         "Математика",
    "WA":           "МХК",
    "BSL":          "ОБЖ",
    "Society":      "Общество",
    "Right":        "Право",
    "Russian":      "Русский язык",
    "Technology":   "Технология",
    "Physics":      "Физика",
    "PC":           "Физра",
    "Chemistry":    "Химия",
    "Ecology":      "Экология",
    "Economics":    "Экономика"
}

if __name__ == "__main__":
    dicts = [files, objects, files_properties, dirs, phrases, versions, types, engchars, ruschars, cards, subjects]
    names = ["files", "objects", "files_properties", "dirs", "phrases", "versions", "types", "engchars", "ruschars",
             "cards", "subjects"]
    for i in range(len(dicts)):
        print('.'*31 + names[i].upper() + '.'*31)
        for key, value in dicts[i].items():
            length = 31 - (len(key) + 1)
            print("{}:{}{}".format(key, ' '*length, _f.paint(value)))
        print()