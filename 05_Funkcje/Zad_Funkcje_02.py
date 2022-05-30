# Napisać funkcję, która sprawdza czy liczba jest parzysta.

number = 0
def is_even(number):
    """This function check is the number is even."""
    number = int(input('podaj liczbę do sprawdzenia ->'))
    if number % 2 == 0:
        print('Your number', number, 'is even.')
    else:
        print('Your number', number, 'is not even.')

is_even(number)
