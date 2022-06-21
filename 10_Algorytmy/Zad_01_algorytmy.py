#  Znajdź największa wspólny dzielnik (NWD) dwóch liczby. Wykorzystaj algorytm Euklidesa.
print('Program oblicza największy wspólny dzielnik dwóch liczb naturalnych.')
first = int(input(f'Podaj pierwszą liczbę całkowitą do sprawdzenia ->'))
second = int(input(f'Podaj drugą liczbę całkowitą do sprawdzenia ->'))


def euklides(first, second):
    a = first
    b = second
    c = first % second
    if c == 0:
        return b
    else:
        first = b
        second = c
    return euklides(first, second)


def main():
    print(f' Największy wspólny dzielnik dla {first} i {second} wynosi {euklides(first, second)}')


if __name__ == "__main__":
    main()

