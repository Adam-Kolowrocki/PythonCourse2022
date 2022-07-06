def check_values(*values):
    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError('Bok musi być wartością numeryczną.')


def rectangle(a, b):
    check_values(a, b)
    return a * b


def triangle(a, h):
    check_values(a, h)
    return 0.5 * a * h


def trapeze(a, b, h):
    check_values(a, b, h)
    return ((a + b) * h) / 2


def main():
    side_A = 6
    side_B = 5
    high_H = 4
    print(rectangle(side_A, side_B))
    print(triangle(side_A, side_B))
    print(trapeze(side_A, side_B, high_H))


if __name__ == "__main__":
    main()
