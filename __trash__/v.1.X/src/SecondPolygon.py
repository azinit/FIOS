import Polygon


def some():
    print('s')
    Polygon.print_field()
    Polygon._f += 1
    Polygon.print_field()


Polygon._f += 1
Polygon.print_field()
some()
