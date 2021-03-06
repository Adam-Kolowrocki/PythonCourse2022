# Poznaj trójkąt Pascala. Napisz kod, który wyświetla trójkąt Pascala dla podanego N.
def data_input():
    user_n = int(input(f'Podaj "N" -> '))
    return user_n


def pascal_triangle(list):
    n = data_input()
    a = []
    i = 0
    for i in range(i ,n):
        a.append([])
        a[i].append((1))
        for j in range(1, i):
            a[i].append(a[i - 1] + a[i - 1][j])
            if (n != 0):
                a[i].append(1)
        for i in range(n):
            print("  " * (n - i), end=" ")
        for j in range(0, i + 1):
            print('{0:6}'.format(a[i][j]), end=" ")
        print()


def main():
    print(f'Program zwracający trójkąt Pascala dla podanej wartości "N"')
    pascal_triangle(list)


if __name__ == "__main__":
    main()
