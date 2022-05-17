# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce.
# Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty.
# Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna,
# 4 i mniej - nie warta uwagi.

title = input('Jaką książke ostatnio czytałeś? ')
print('Oceń książkę', title, 'podając oceny w skali 1-10, gdzie 1 to ocena najgorsza a 10 to ocena najlepsza.')
story = float(input(f'Oceń fabułę książki {title}:'))
cover = float(input(f'Oceń okładkę ksiażki {title}:'))
graphics = float(input(f'Oceń ilustracje w książce {title}:'))

average = (story + cover + graphics) / 3

if average > 7:
    print(title, 'jest bardzo dobra.')
elif average >= 5:
    print(title, 'jest przeciętna.')
else:
    print(title, 'nie jest warta uwagi.')

