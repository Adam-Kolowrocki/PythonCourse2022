# Utwórz plik zawierający listę ok. 20 cytatów.
# Każdy cytat powinien się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
# Quote of the day is:
# **************************************
#            be or not to be?
# **************************************
# zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami.
# Plik z cytatami powinien również zawierać informację o autorze, wyświetl cytat i pod spodem autora

import random


def losowanie():
    file_to_open = input(f'Podaj nazwę pliku z cytatami (pomiń rozszerzenie) -> ')
    with open(file_to_open + '.txt', 'r') as file:
        content = file.readlines()

    cytat_na_dzis = random.choice(content)
    return cytat_na_dzis


def show(cytat_na_dzis):
    cytat_na_dzis = cytat_na_dzis.strip('\n')
    cytat_na_dzis = cytat_na_dzis.split('||')
    length = len(cytat_na_dzis) + 20
    print('\nCytat dnia to:\n')
    print('*' * length)
    print(cytat_na_dzis[0])
    print('*' * length)
    print(f'A jego autorem jest: ')
    print('*' * length)
    print(cytat_na_dzis[1])
    print('*' * length)


def main():
    cytat_na_dzis = losowanie()
    show(cytat_na_dzis)


if __name__ == "__main__":
    main()
