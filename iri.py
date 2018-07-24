import inspect
import datetime

import FIOS.notifier as _note
from FIOS.cfg import Settings as _Settings
from FIOS.font import beige as _beige, beige2 as _beige2, paint as _p, blackbg as _blackbg, end as _end
from FIOS.sample import versions as _vs
from FIOS.convert import to_hms as _to_hms

start_time, end_time = 0, 0
csl_color, emit_color = _beige, _beige2

USER = _Settings().user
AI = _Settings().assistant
AI_full = _Settings().assistant_full
AI_ico = _p("👩 ", csl_color)


def launch(project="", mode="Test"):
    project = str(inspect.stack()[1][1]).split('/')[::-1][0] if not project else project

    def info(info_struct):
        version = _vs["iri"]
        _note.message_box("{} vs. {}".format(AI_full, version), b_m=7, b_pat='.', color=_blackbg + csl_color)
        _note.time.sleep(0.3)
        print()
        _note.parameters(info_struct)

    def greeting(offset=False):
        print() if offset else None
        _note.message_console("Hello, {}!".format(USER), c_pat=AI_ico, time_delay=0.2)
        _note.message_console("I'm {} :)".format(AI), c_pat=AI_ico, time_delay=0.2)
        # TODO: Intersection colors
        # note.message_console("I'm {}{} :) {}".format(font.bold, AI, font.end, ''), c_pat=AI_ico, time_delay=0.2)
        _note.message_console("I'll be your assistant".format(_p(AI, emit_color)), c_pat=AI_ico)

    def set_time():
        global start_time
        start_time = datetime.datetime.now()

    info({"Time": str(datetime.datetime.now()), "Project": project, "Mode": mode})
    greeting(True)
    set_time()
    _note.status('=', '=', color=csl_color)


def shutdown():
    def info(diff):
        _note.message_console(_p("{} finishing".format("Process"), csl_color), c_pat='')
        _note.message_console("In: {}{}h:{}m:{}s{}".format(emit_color, diff[0], diff[1], diff[2], _end), c_pat='')

    def get_work_time():
        global start_time, end_time
        end_time = datetime.datetime.now()
        work_time = (end_time - start_time).total_seconds()
        return _to_hms(work_time)

    def goodbye(offset=False):
        print() if offset else None
        _note.message_console("Fuh...After all, we worked well, didn't we? ;)", c_pat=AI_ico)
        _note.message_console("See you soon", c_pat=AI_ico)
        _note.message_console("Your {}".format(_p(AI, emit_color)), c_pat=AI_ico)

    _note.status('=', '=', color=csl_color)
    info([str(int(x)) for x in get_work_time()])
    goodbye()


if __name__ == "__main__":
    launch()
    print("// Some magic ¯\_(ツ)_/¯")
    _note.time.sleep(2)
    shutdown()
