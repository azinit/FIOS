import inspect

import FIOS.notifier as note

sample, cfg = note.smp, note.convert.cfg
font, datetime = sample.font, sample.datetime

start_time, end_time = 0, 0
csl_color, emit_color = font.beige, font.beige2

USER = cfg.Settings().user
AI = cfg.Settings().assistant
AI_full = cfg.Settings().assistant_full
AI_ico = font.paint("👩 ", csl_color)


def launch(project="", mode="Test"):
    project = str(inspect.stack()[1][1]).split('/')[::-1][0] if not project else project

    def info(info_struct):
        version = sample.versions.get("iri")
        note.message_box("{} vs. {}".format(AI_full, version), b_m=7, b_pat='.', color=font.blackbg + csl_color)
        note.time.sleep(0.3)
        print()
        note.parameters(info_struct)

    def greeting(offset=False):
        print() if offset else None
        note.message_console("Hello, {}!".format(USER), c_pat=AI_ico, time_delay=0.2)
        note.message_console("I'm {} :)".format(AI), c_pat=AI_ico, time_delay=0.2)
        # TODO: Intersection colors
        # note.message_console("I'm {}{} :) {}".format(font.bold, AI, font.end, ''), c_pat=AI_ico, time_delay=0.2)
        note.message_console("I'll be your assistant".format(font.paint(AI, emit_color)), c_pat=AI_ico)

    def set_time():
        global start_time
        start_time = datetime.datetime.now()

    info({"Time": str(datetime.datetime.now()), "Project": project, "Mode": mode})
    greeting(True)
    set_time()
    note.status('=', '=', color=csl_color)


def shutdown():
    def info(diff):
        note.message_console(font.paint("{} finishing".format("Process"), csl_color), c_pat='')
        note.message_console("In: {}{}h:{}m:{}s{}".format(emit_color, diff[0], diff[1], diff[2], font.end), c_pat='')

    def get_work_time():
        global start_time, end_time
        end_time = datetime.datetime.now()
        work_time = (end_time - start_time).total_seconds()
        return note.convert.to_hms(work_time)

    def goodbye(offset=False):
        print() if offset else None
        note.message_console("Fuh...After all, we worked well, didn't we? ;)", c_pat=AI_ico)
        note.message_console("See you soon", c_pat=AI_ico)
        note.message_console("Your {}".format(font.paint(AI, emit_color)), c_pat=AI_ico)

    note.status('=', '=', color=csl_color)
    info([str(int(x)) for x in get_work_time()])
    goodbye()


if __name__ == "__main__":
    launch()
    print("// Some magic ¯\_(ツ)_/¯")
    note.time.sleep(2)
    shutdown()
