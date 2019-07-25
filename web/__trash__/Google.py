# def search(search_term, **kwargs):
#     from gsearch.googlesearch import search
#     num = kwargs.get("num", 5)
#
#     results = search('Avi Aryan', num_results=num)
#     return results



# def search__():
#     from fios.web import webkit
#     user = webkit.get_user(ip=True)
#     agent, proxy = user["User-Agent"], user["http"]
#     # Get the first 20 hits for: "Breaking Code" WordPress blog
#     from googlesearch import search
#     for url in search('"Breaking Code" WordPress blog', stop=20, user_agent=agent):
#         print(url)
#
#
# def search_custom():
#     def generate_request(keywords):
#         sep = "+"   # %20
#         term = sep.join(keywords)
#         url = 'https://www.google.com/search?q={term}'.format(term=term)
#         return url
#
#     def get_results(url):
#         from fios.web import webkit
#         soup = webkit.soupify(url)
#         # soup = webkit.soupify(url, features='lxml')
#         print(soup.prettify())
#         # links = soup.select('.rc ')
#         # links = soup.find_all("div", class_="rc")
#         # [print(x) for x in links]
#
#     # keywords = ["mortal", "kombat"]
#     keywords = ["wordpress"]
#     request = generate_request(keywords)
#     results = get_results(request)


if __name__ == '__main__':
    __results = search("")

    # show_results(__results)
    for result in __results:
        print(result)

    # for key, value in results[0].items():
    #     print(key.ljust(20), ":", value)


