# Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość
# z 3 liczb. minimum_of(a, b, c).

def numbers():
    print(f'Podaj 3 liczby do porównnia')
    a = int(input(f'Podaj liczbę a = '))
    b = int(input(f'Podaj liczbę b = '))
    c = int(input(f'Podaj liczbę c = '))
    return a, b, c


a, b, c = numbers()

def minimum_of(a, b, c):
    if a > b < c:
        print(f'Wartość {b} jest najmniejsza.')
    elif b > a < c:
        print(f'Wartość {a} jest najmniejsza.')
    else:
        print(f'Wartość {c} jest najmniejsza.')
    return


minimum_of(a, b, c)