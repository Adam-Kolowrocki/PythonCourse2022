# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def is_even(number):
    """This function check is the number is even."""
    if number % 2 == 0:
        print('Your number', number, 'is even.')
    else:
        print('Your number', number, 'is not even.')

is_even(number = int(input('Podaj liczbę do sprawdzenia -> ')))
