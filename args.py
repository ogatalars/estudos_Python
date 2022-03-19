# args = parameter that wil pack all arguments into a tuple. Useful so that a function can accept multiple arguments.

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3))


def minus(*args):
    minus = 0
    for i in args:
        minus -= i
    return minus


print(minus(1, 2, 3, 4, 4, 5))
