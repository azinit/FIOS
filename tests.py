# TODO: locales


def __len(b):
    return len(b) > 2


def foo(b: list):
    b.pop()


def bar(b: list):
    b.pop()
    b.pop()


def zoc(b: list):
    b.pop()
    b.pop()
    b.pop()
    b.pop()
    b.pop()
    b.pop()


if __name__ == '__main__':
    # TODO: !!!
    l = format("[%s] Lak", '1')
    print(l)
    try:
        print(1 / 1)
    except Exception as e:
        l = e.with_traceback(e.__traceback__)
        print(l)

    a = [1, 2, 3, 4, 5, 6, 7, 8]

    # while __len(a):
    #     print(0)
    #     zoc(a)
    #     print(1)
    #     foo(a)
    #     print(2)
    #     bar(a)
    #     print(3)

    b = [1, 2, 3]
    c = [1, 3]
    d = [1]

    user = {
        "user_1": {
            "age": 13
        }
    }
    if b in d:  print("b in d")
    if c in d:  print("c in d")
    if d in c:  print("d in c")
    if c in b:  print("c in b")
    print(user["user_1__age"])