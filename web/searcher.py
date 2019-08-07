"""
..............................................................................................................
................................................ GOOGLE SEARCH ...............................................
..............................................................................................................
"""


def google(search_term, **kwargs):
    # https://stackoverflow.com/questions/38635419/searching-in-google-with-python
    # https://linuxhint.com/google_search_api_python/
    from googleapiclient.discovery import build

    # CSE: https://cse.google.com/cse/setup/basic?cx=001635399101945400726:2pnxzsd7mai
    # API: https://console.developers.google.com/iam-admin/settings?project=caseparser-1563876097685&authuser=0&folder=&organizationId=

    # init.bridge@gmail.com
    # API_KEY = "AIzaSyBVxBWaCSi9QvBbeYDm0pOUyax4tKeECZo"
    # CSE_ID = "001635399101945400726:2pnxzsd7mai"

    # azin271@gmail.com
    API_KEY = "AIzaSyCWe6D4CMG5u4Sfs6TxjUIBdnY6f9ovE50"
    CSE_ID = "013147149367356599732:zfoch_9w010"

    num = kwargs.get("num", 5)

    service = build("customsearch", "v1", developerKey=API_KEY)
    res = service.cse().list(q=search_term, cx=CSE_ID, num=num, **kwargs).execute()

    # extended = kwargs.get("extended", False)
    # if not extended:

    return {"engine": "google", "results": res['items']}


"""
..............................................................................................................
................................................ YANDEX SEARCH ...............................................
..............................................................................................................
"""


def yandex(term, **kwargs):
    import yandex_search

    # TODO: IP

    # https://xml.yandex.ru/limits/
    num = kwargs.get("num", 5)

    API_USER = "martis-boolean"
    API_KEY = "03.909492691:e52aa52332f8301adf2f56de3f9495c1"

    searcher = yandex_search.Yandex(api_user=API_USER, api_key=API_KEY)
    try:
        results = searcher.search(term).items
    except yandex_search.ConfigException:
        input("Ваш IP сменился.\nОбновите его, пожалуйста, для поисковой машины (нажмите Enter) ")
        input("Обновили? (нажмите Enter)")
        print("Идем дальше!")
        return yandex(term, **kwargs)
    return {"engine": "yandex", "results": results[:num:]}


"""
..............................................................................................................
................................................ SHOW RESULTS ................................................
..............................................................................................................
"""


def show_results(data: dict):
    engine      = data["engine"]
    results     = data["results"]

    key_title   = "title"
    key_url     = "url" if engine == "yandex" else "link"
    key_snippet = "snippet"

    for item in results:
        print("TITLE:  ", item[key_title])
        print("URL:    ", item[key_url])
        print("DESC:   ", item[key_snippet])
        print()


"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""

if __name__ == '__main__':
    def __test__yandex():
        print(":::::::::::::::::::::yandex:::::::::::::::::::::")
        # terms = ["python", "java", "js", "react", "graphql"]
        terms = ["coca femsa sab de cv", "ciner resources lp", "codorus valley bancorp inc", "cnx midstream partners lp",
                 "clearside biomedical inc", "european partners plc"]
        from fios.web import webkit
        import time
        for term in terms:
            print("SEARCH: ", term)
            print("-"*999)
            # print(webkit.get_user(ip=True, agent=False, current=True))
            results = yandex(term, num=10)
            show_results(results)
            print("="*999)
            print()
            time.sleep(5)




    __test__yandex()
