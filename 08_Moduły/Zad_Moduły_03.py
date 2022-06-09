# Stwórz moduł, który zajmuje się jedynie otwieraniem plików
# - oferuje bezpieczny sposób odczytu oraz bezpieczny zapis.
# Funkcja czytająca pliki sprawdza najpierw czy dany plik istnieje
# oraz czy jest niepusty. Funkcja zapisująca do pliku chroni
# przed nadpisaniem istniejącego pliku.

import os

filename = input(f'podaj nazwę pliku do otwarcia ->')
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('Nie ma takiego pliku')
