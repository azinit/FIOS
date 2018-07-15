import datetime
import inspect

import FIOS.font as font


start_time = 0
end_time = 0


def launch(project="", mode="Test"):
    project = str(inspect.stack()[1][1]).split('/')[::-1][0] if not project else project
    print(' | version: %s | font version: %s')


if __name__ == "__main__":
    launch()
