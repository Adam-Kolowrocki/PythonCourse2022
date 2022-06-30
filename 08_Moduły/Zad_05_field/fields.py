pi = 3.14


def square(a):
    return a * a


def rectangle(a, b):
    return a * b


def triangle(a, h):
    return (a / 2) * h


def circle(r):
    global pi
    return pi * (r * r)


def trapeze(a, b, h):
    return ((a + b) * h) / 2


def diamond(a, h):
    return a * h

