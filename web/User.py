import random
from webkit import webkit


class User(object):

    def __init__(self, user_agent=None, proxy=None):
        if user_agent is None and proxy is None:
            self.user_agent = random.choice(webkit.load_user_agent())
            self.proxy = random.choice("http://" + str(webkit.load_proxies()))
        else:
            self.user_agent = user_agent
            self.proxy = proxy

    def __str__(self):
        return str(
            "<==================== {} ====================>\n{}".format(self.proxy, split_seq(self.user_agent, 50)))


def split_seq(string, seq_len):
    return '\n'.join([string[i:i + seq_len] for i in range(0, len(string), seq_len)])
