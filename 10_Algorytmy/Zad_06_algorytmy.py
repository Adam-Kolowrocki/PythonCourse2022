# Poznaj trójkąt Pascala. Napisz kod, który wyświetla trójkąt Pascala dla podanego N.
def data_input():
    user_n = int(input(f'Podaj "N" -> '))
    return user_n


def pascal_triangle():
    n = data_input()


def main():
    print(f'Program zwracający trójkąt Pascala dla podanej wartości "N"')
    pascal_triangle()


if __name__ == "__main__":
    main()