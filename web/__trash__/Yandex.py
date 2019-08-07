import yandex_search

# TODO: IP


def search(term, **kwargs):
    # https://xml.yandex.ru/limits/
    # 26.07.19: ip: 84.39.247.25
    num = kwargs.get("num", 5)

    API_USER = "martis-boolean"
    API_KEY = "03.909492691:e52aa52332f8301adf2f56de3f9495c1"

    yandex = yandex_search.Yandex(api_user=API_USER, api_key=API_KEY)
    results = yandex.search(term).items
    return results[:num]

# [{
#       "snippet": "Your Software Development Partner In  Saudi   Arabia . Since our early days in 2003, our main goal in  Interactive   Saudi   Arabia  has been: \"To earn customer respect and maintain long-term loyalty\".",
#       "url": "http://www.interactive.sa/en",
#       "title": "Interactive   Saudi   Arabia  Limited",
#       "domain": "www.interactive.sa"
# }]


def show_results(results):
    for result in results:
        print("[%s]" % result["title"])
        print(result["url"])
        print(result["snippet"])
        print()


if __name__ == '__main__':
    results = search('ethereum')
    show_results(results)
