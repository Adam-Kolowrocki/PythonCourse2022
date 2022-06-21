# Napisz kod, który zwraca sumę wszystkich wielokrotności 5 lub 7 poniżej liczby N.
# Na przykład dla 21 mamy: 5, 7, 10, 14, 15, 20, stąd wynik 71
print(f'Program zwraca sumę wielokrotności 5 i 7 w zakresie od 1 do podanej liczby N.')
user_N = int(input(f'Podaj wartość "N" -> '))


def sum_5_7():
    sum = 0
    for i in range(1, user_N):
        if i % 5 == 0 or i % 7 == 0:
            sum += i
    return sum


def main():
    print(f' Suma wielokrotności 5 i 7 w zakresie od 1 do {user_N} wynosi {sum_5_7()}')


if __name__ == "__main__":
    main()
