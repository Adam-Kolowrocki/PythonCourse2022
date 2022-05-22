# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik,
# w przeciwnym wypadku wyświetl “Koniec”.

first_digit = int(input('Podaj pierwszą liczbę całkowitą:'))
second_digit = int(input('Podaj drugą liczbę całkowitą:'))
sum = first_digit + second_digit
if sum >= 100:
    print(f'Suma Twoich liczb wynosi {sum}.')
else:
    print('Koniec')