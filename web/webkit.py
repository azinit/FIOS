import os
import time

import requests
from bs4 import BeautifulSoup
from fios.io import console

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
THREAD_NAME = "WEBKIT"

URL_USER_INFO = "http://sitespy.ru/my-ip"
URL_PROXIES_1 = "https://www.ip-adress.com/proxy-list"
URL_PROXIES_2 = "https://free-proxy-list.net/"

# TODO: ip_wrapper (http)
"""
..............................................................................................................
................................................ HTML: SUMMARY ...............................................
..............................................................................................................
"""


def load(url, **kwargs):
    # TODO: add https
    # Proxy bind only with Agent!
    """ Load HTML content of page """
    # init kwargs
    notify  = kwargs.get("notify",  False)
    proxy   = kwargs.get("proxy",   False)
    agent   = kwargs.get("agent",   proxy)
    timeout = kwargs.get("timeout", 5)
    as_text = kwargs.get("as_text", True)
    options = {}
    # fill options
    if notify:                      console.log(message="{url} is loading...", thread=THREAD_NAME)
    if agent:                       options["headers"] = {"User-Agent": get_user() if agent is True else agent}
    if proxy:                       options["proxies"] = {"http": get_proxy(url) if proxy is True else proxy}
    if isinstance(timeout, int):    options["timeout"] = timeout
    # get response
    response = requests.get(url, **options)
    return response.text if as_text else response


def soupify(url, **kwargs):
    """ Get soup of page """
    html = load(url, **kwargs)
    soup_ = BeautifulSoup(html, features="html.parser")
    return soup_


"""
..............................................................................................................
................................................ USER: SUMMARY ...............................................
..............................................................................................................
"""


def get_user(**kwargs):
    current         = kwargs.get("current", False)
    agent           = kwargs.get("agent", True)
    ip              = kwargs.get("ip",      False)
    url             = kwargs.get("url",     URL_USER_INFO)

    user = {}

    if current:
        soup = soupify(url=URL_USER_INFO)
        div         = soup.find("div", class_="ip-block")
        my_ip       = div.span.text
        my_agent    = div.span.find_next_sibling("span").text

        if ip:      user["http"] = "http://" + my_ip
        if agent:   user["User-Agent"]  = my_agent
    else:
        import random
        agents = load_agents()

        if ip:      user["http"] = get_proxy(url)
        if agent:   user["User-Agent"] = random.choice(agents)

    return user


"""
..............................................................................................................
................................................ PROXY: SUMMARY ..............................................
..............................................................................................................
"""


def refresh_proxies(**kwargs):
    # inner proxies getting

    def __proxies_1(**kwargs_):
        soup = soupify(URL_PROXIES_1)
        tr = soup.find("tbody").find_all("tr")
        __proxies = []
        for i, x in enumerate(tr):
            a = x.td.a
            ip = a.text
            port = a.next_sibling
            # __proxies.append("http://" + ip + port)
            __proxies.append(ip + port)
            __progress(done=i + 1, total=len(tr), **kwargs_)
        return __proxies

    def __proxies_2(**kwargs_):
        soup = soupify(URL_PROXIES_2)
        tr = soup.find("table", class_="table").tbody.find_all("tr")
        __proxies = []
        for i, x in enumerate(tr):
            td      = x.find_all("td")
            ip      = td[0].text
            port    = td[1].text
            # __proxies.append("http://" + ip + ":" + port)
            __proxies.append(ip + ":" + port)
            __progress(done=i + 1, total=len(tr), **kwargs_)
        return __proxies

    def __proxies_3(**kwargs_):
        __progress(done=1, total=1, **kwargs_)
        return []
    # ...................................................................
    notify = kwargs.get("notify", False)

    proxies = [*__proxies_1(title="Refreshing proxies [1/3]", notify=notify),
               *__proxies_2(title="Refreshing proxies [2/3]", notify=notify),
               *__proxies_3(title="Refreshing proxies [3/3]", notify=notify)]
    # __save_proxies(proxies)   TODO:
    return proxies


# TODO: dev!
def filter_proxies(proxies: list, url: str, **kwargs):
    # TODO:  if not proxies: common list
    notify = kwargs.get("notify", False)

    filtered = proxies.copy()

    for i, p in enumerate(proxies):
        try:
            # TODO: load instead get
            r = requests.get(url, proxies={"http": p})
            if r.status_code != 200:
                filtered.remove(p)
        except requests.exceptions.ConnectionError:
            filtered.remove(p)

        __progress(title="Filtering proxies", done=i + 1, total=len(proxies), notify=notify)

    print("{} -> {}".format(len(proxies), len(filtered)))
    return proxies


def get_proxy(url, **kwargs):
    # init kwargs
    notify      = kwargs.get("notify", False)
    proxies     = kwargs.get("proxies", load_proxies())
    http_wrap   = kwargs.get("http_wrap", True)
    # load_options
    __load_options = kwargs.copy()
    __load_options["as_text"] = False
    __load_options["notify"] = False

    for i, proxy in enumerate(proxies):
        try:
            __progress(title="Getting proxy", done=i + 1, total=len(proxies), notify=notify)
            # r = requests.get(url, proxies={'http': proxy})
            r = load(url, proxy=proxy, **__load_options)
            if r.status_code == 200:
                __progress(title="Getting proxy", done=i + 1, total=len(proxies), notify=notify, _finish_force=True)
                if http_wrap: proxy = "http://" + proxy
                return proxy
        except requests.exceptions.ConnectionError:
            continue
    else:
        refresh_proxies()
        return get_proxy(url)


"""
..............................................................................................................
................................................ INNER IO ....................................................
..............................................................................................................
"""


def __progress(title, done, total, notify=True, **kwargs):
    if notify: console.progress(
        title=title,
        done=done,
        total=total,
        allowed_iterator=True,
        allowed_percent=False,
        **kwargs
    )


# SAVING #
def __save_proxies(proxies):
    __save_list("proxies.txt", "\n".join(proxies))


def __save_list(file_list, content):
    os.chdir(CUR_DIR)
    with open(file_list, 'w') as file:
        file.write(content)


# LOADING #
def load_proxies():
    return __load_list("proxies.txt")


def load_agents():
    import json
    with open('agents.json', 'r') as json_file:
        data = json.load(json_file)
    return data["agents"]


def __load_list(file_list):
    # TODO: chdir issue : in exe
    os.chdir(CUR_DIR)
    with open(file_list, 'r') as file:
        content = file.read().split('\n')
    return content


"""
..............................................................................................................
................................................ TESTS .......................................................
..............................................................................................................
"""
if __name__ == '__main__':
    test_set = [
        "https://www.shutterstock.com/ru/g/sharafmaksumov?searchterm=screen+site&search_source=base_gallery&language=ru&page=1&sort=popular&exclude_keywords=mobile&measurement=px&safe=true"
    ]

    def __test__refresh():
        print(":::refresh:::")
        proxies = refresh_proxies(notify=True)
        return proxies

    def __test__proxy():
        print(":::proxy:::")
        # p = get_proxy(url=test_set[0], notify=True, proxies=proxies)
        p = get_proxy(url=test_set[0], notify=True)
        print(p)

    def __test__filter():
        print(":::filter:::")
        filtered = filter_proxies(proxies=load_proxies()[:50], url=test_set[0], notify=True)
        print(filtered)
        filtered = filter_proxies(proxies=proxies[:50], url=test_set[0], notify=True)
        print(filtered)

    def __test__get_user():
        print(":::get_user:::")
        # print(get_user(current=True))
        # print(get_user(current=True, agent=False, ip=True))
        # print(get_user(current=True, agent=False, ip=False))
        # print(get_user(current=True, ip=True))
        # print(get_user(agent=True, ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))
        print(get_user(ip=True))


    proxies = __test__refresh()
    # __test__proxy()
    # __test__filter()
    __test__get_user()
