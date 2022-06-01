# Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”,
# “nie, liczba x jest z poza zakresu”.

def data_input():
    range_start = int(input(f'Podaj początkową wartość zakresu -> '))
    range_end = int(input(f'Podaj końcową wartość zakresu -> '))
    looking_num = int(input(f'Podaj liczbę, którą mam znaleźć -> '))
    return range_start, range_end, looking_num


range_start, range_end, looking_num = data_input()


def test_func(range_start, range_end, looking_num):
    if range_start < range_end and range_start <= looking_num <= range_end:
        print(f'Tak, liczba {looking_num} znajduje się w zadanym zakresie.')
    elif range_start > range_end and range_start >= looking_num >= range_end:
        print(f'Tak, liczba {looking_num} znajduje się w zadanym zakresie.')
    else:
        print(f'Nie, liczba {looking_num} jest z poza zakresu.')
    return

test_func(range_start, range_end, looking_num)

