# Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

# numbers = [2, 3, 6, 7, 8, 4, 5]
numbers = []
while len(numbers) < 10:
    user = int(input('Podaj liczbę ->'))
    numbers.append(user)

print('Podałeś następujace liczby: ', numbers)
nieparzyste = []
for n in numbers:
    if n % 2 != 0:
        nieparzyste.append(n)
print('Z podanych przez Cieie liczb', numbers, 'nieparzyste są:', nieparzyste)