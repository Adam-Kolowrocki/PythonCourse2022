# Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą maksymalną wartość z 3 liczb.
# maximum_of(a, b, c).


def numbers():
    print(f'Podaj 3 liczby do porównania')
    a = int(input(f'Podaj liczbę a = '))
    b = int(input(f'Podaj liczbę b = '))
    c = int(input(f'Podaj liczbę c = '))
    return a, b, c


a, b, c = numbers()


def minimum_of(a, b, c):
    if a < b > c:
        print(f'Wartość {b} jest największa.')
    elif b < a > c:
        print(f'Wartość {a} jest największa.')
    else:
        print(f'Wartość {c} jest największa.')
    return


minimum_of(a, b, c)