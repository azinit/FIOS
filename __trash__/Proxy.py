import requests
from bs4 import BeautifulSoup


class Proxy(object):
    proxy_url = "https://www.ip-adress.com/proxy-list"
    proxy_list = []

    def __init__(self):
        r = requests.get(self.proxy_url)
        soup = BeautifulSoup(r.content, features="html.parser")
        tr = soup.find("tbody").find_all("tr")
        print("[P] Getting proxies.", end='')
        for x in tr:
            a = x.td.a
            ip = a.text
            port = a.next_sibling
            self.proxy_list.append("http://" + ip + port)
            print(".", end='')
        print()

    def get_proxy(self):
        for proxy in self.proxy_list:
            try:
                r = requests.get('http://rutracker.org', proxies={'http': proxy})
                if r.status_code == 200:
                    print(BeautifulSoup(r.content).prettify())
                    return proxy
            except requests.exceptions.ConnectionError:
                continue


proxy = Proxy()
proxy = proxy.get_proxy()
# r = requests.get(url, proxies={'http': proxy})
# print(r.status_code)
# print(r.content)
