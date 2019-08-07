def __sys_time():
    from datetime import datetime
    sys_time = datetime.now().strftime("%H:%M:%S")
    return "[%s] " % sys_time


def write(*values, **kwargs):
    """ Extended print analogue """
    sep         = kwargs.get("sep", " ")
    end         = kwargs.get("end", "\n")
    # file      = kwargs.get("file", None)      # TODO:
    flush       = kwargs.get("flush", False)
    color       = kwargs.get("color", None)     # TODO:
    # TODO: sys_time?

    if flush:
        import sys
        sys.stdout.write("\r" + sep.join(values))
        sys.stdout.flush()
    else:
        print(*values, sep=sep, end=end)

# TODO: table


def ask(question, **options):
    # TODO: Extend: Yes/No => Variants/Codes
    label_yes = options.get("label_yes", "Y")
    label_no  = options.get("label_no",  "N")
    code_yes  = options.get("code_yes",  True)
    code_no   = options.get("code_no",   False)
    skip      = options.get("skip", None)

    formatted_question = "{question} [{vars}]\n>>> ".format(
        question=question,
        vars="/".join([label_yes, label_no])
    )
    response = str(input(formatted_question)).lower()
    if response == label_yes.lower():
        return code_yes
    elif response == label_no.lower():
        return code_no
    else:
        log("< Повторяем вопрос >")
        return ask(question, **options)


def log(message, **kwargs):
    """ Log message with os date """
    thread = kwargs.get("thread", None)
    from datetime import datetime
    sys_time = datetime.now().strftime("%H:%M:%S")
    write("[{sys_time}]{thread} {message}".format(
        sys_time=sys_time,
        thread="" if thread is None else " [%s]" % thread,
        message=message,
    ), **kwargs)


def error(message, **kwargs):
    # TODO:
    pass

# TODO: process: Process . . . . DONE!
# TODO: start_process? : ... Process ...


def process(title, **kwargs):
    """ Print process header with decorators """
    width               = kwargs.get("width", 32)
    symb                = kwargs.get("symb", ".")
    indent              = kwargs.get("indent", True)
    allowed_sys_time    = kwargs.get("allowed_sys_time", False)

    # indent case
    if indent:
        title = " %s " % title
    # init pattern constructor
    pattern = ":{symb}^{width}".format(
        symb=symb,
        width=width,
    )
    pattern = "{%s}" % pattern
    # fill pattern
    msg = "{time}{msg}".format(
        time=allowed_sys_time * __sys_time(),
        msg=pattern.format(title),
    )
    write(msg, **kwargs)


def wait(callback):
    import time
    while not callback():
        steps = ["\\", "|", "/", "-"]
        for s in steps:
            write(s, flush=True)
            time.sleep(0.1)


# TODO: 0, 1, 2,.... 99, 100? | total - 1
# TODO: thread?
def progress(title, done, **kwargs):
    # TODO: Final term
    # TODO: Few lines
    """ Print progress [...] in console """
    #     "|████████                             | 24.7MB 3.2MB/s eta 0:00:25"
    #     "|█████████████████               | 54.6MB 6.4MB/s eta 0:00:08"
    # TODO: tqdm?

    # init local functions
    def __extra():
        return (extra_data is not None) * (" | " + str(extra_data))

    # def __sys_time():
    #     from datetime import datetime
    #     sys_time = datetime.now().strftime("%H:%M:%S")
    #     return allowed_sys_time * ("[%s] " % sys_time)

    def __finished():
        return percent >= 100 or _finish_force

    def __bar():
        bar = "{done}{undone}".format(
            done    = symb_done     * block_done,
            undone  = symb_undone   * block_undone,
        )
        return allowed_bar * bar

    def __state():
        return allowed_state * ((symb_finished if __finished() else symb_wait) + " ")

    def __percent():
        return allowed_percent * ("{0:.2f}%".format(percent))

    def __iterator():
        return allowed_iterator * "{done}/{total}".format(done=done, total=total)

    # def __watchers():
    #     watchers = [__percent(), __iterator()]
    #     watchers = list(map(lambda x: "[%s]" % x, watchers))
    #     separator = " "
    #     return separator.join(watchers)
    # init kwargs
    total               = kwargs.get("total",               100)
    length              = kwargs.get("length",              32)

    symb_wait           = kwargs.get("symb_wait",           "⟲")
    symb_finished       = kwargs.get("symb_finished",       "✔")
    symb_done           = kwargs.get("symb_done",           '▰')
    symb_undone         = kwargs.get("symb_undone",         '▱')

    allowed_state       = kwargs.get("allowed_state",       True)
    allowed_bar         = kwargs.get("allowed_bar",         False)
    allowed_percent     = kwargs.get("allowed_percent",     True)
    allowed_iterator    = kwargs.get("allowed_iterator",    False)
    allowed_sys_time    = kwargs.get("allowed_sys_time",    False)

    extra_data          = kwargs.get("extra_data",          None)
    _finish_force       = kwargs.get("_finish_force",       False)

    # compute percent cases
    if done == total == 0: done, total = 1, 1

    percent = done if total is 100 else (float(done) / total) * 100
    # percent = round(percent, 2)
    # compute blocks amount
    block_done          = int(round(length * percent / 100))
    block_undone        = length - block_done

    # compute message
    msg = "{time}{state}{title}: {bar} {percent} {iterator}{extra}".format(
        time=allowed_sys_time * __sys_time(),
        state=__state(),
        title=title,
        bar=__bar(),
        percent=__percent(),
        iterator=__iterator(),
        extra=__extra(),
    )
    if __finished():
        msg += "\r\n"
    # show message
    write(msg, flush=True)


def result(item, state, **kwargs):
    # TODO: symb?
    thread      = kwargs.get("thread", None)
    patterns    = kwargs.get("patterns", None)

    are_valid_patterns = len(patterns) >= 2
    if are_valid_patterns: log(message=patterns[state] % item, thread=thread)


def box(message, **kwargs):
    # TODO: Abs
    from fios.util import fstring
    box_ = fstring.put(message, **kwargs)
    write(box_, **kwargs)


if __name__ == '__main__':
    def __test__log():
        print(":::::::::::::::::::::log:::::::::::::::::::::")
        log("Hello!")
        log(message="Hello")
        log("Lop", thread="AP")
        log([1, 2, 3])
        log("Message #1", flush=True)
        log("Message #2", flush=True)
        log("Message #3", flush=True)

    def __test__process():
        print(":::::::::::::::::::::process:::::::::::::::::::::")
        # process("L")
        process(
            title="TITLE",
            indent=True,
            width=100,
            symb="/"
        )

        process(
            title="PROCESS",
            indent=True,
            width=64,
            allowed_sys_time=True,
        )

    def __test__write():
        print(":::::::::::::::::::::write:::::::::::::::::::::")
        write("dw", flush=True)
        write("dw", flush=True)
        write("dw", flush=False)
        write("dw", flush=False)
        write("---", "EXCEL", "WRITE", "ROW", "WORK!@#FA%D#$@LF@")

    def __test__progress():
        print(":::::::::::::::::::::progress:::::::::::::::::::::")
        import time
        limit = 32
        for i in range(limit):
            time.sleep(0.02)
            # _finish = i == 27
            _finish = False
            progress(
                title="PROCESS",
                length=10,
                done=i,
                total=limit - 1,
                symb_wait="?",
                symb_finished="!",
                symb_done="/",
                symb_undone=".",
                allowed_bar=True,
                allowed_state=True,
                allowed_percent=True,
                allowed_iterator=True,
                allowed_sys_time=False,
                _finish_force=_finish,
            )
            if _finish:
                break

    def __test__ask():
        print(":::::::::::::::::::::ask:::::::::::::::::::::")
        print(ask("1. Можно кратко, Да или Нет?"))
        print(ask("2. Можно кратко, Да или Нет?"))
        print(ask("3. Можно кратко, Да или Нет?"))
        print(ask("4. Можно кратко, Да или Нет?"))


    def __test__wait():
        print(":::::::::::::::::::::wait:::::::::::::::::::::")
        wait(lambda: False)
    # ........................................................................................................
    # __test__log()
    # __test__process()
    # __test__write()
    # __test__progress()
    # __test__progress()
    # __test__progress()
    # __test__progress()
    # __test__ask()
    __test__wait()
