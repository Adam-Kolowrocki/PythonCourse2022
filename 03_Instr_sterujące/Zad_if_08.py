# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

first = float(input('Podaj pierwszą liczbę: '))
second = float(input('Podaj drugą liczbę: '))
third = float(input('Podaj trzecią liczbę: '))

if first > second and third:
    print('Pierwsza liczba jest największa.')
elif second > third:
    print('Druga liczba jest największa. ')
else:
    print('Trzecia liczba jest największa. ')

list = [first, second, third]
print(sorted(list))
