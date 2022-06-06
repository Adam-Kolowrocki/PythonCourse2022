# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów.
# Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję,
# która losuje i wyświetla w sposób ciekawy cytat na dziś. Np. można wyświetlić tak:
#
# Quote of the day is:
#
# **************************************
#            be or not to be?
# **************************************
#
#     zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
#
#     plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

import random


def losowanie():
    with open('cytaty.txt') as file:
        content = file.readline()

    cytat_na_dzis = random.choice(content)
    return cytat_na_dzis


def show(cytat_na_dzis):
    cytat_na_dzis = cytat_na_dzis.strip('\n')
    lenth = len(cytat_na_dzis) + 20
    print('\nCytat dnia to:\n')
    print('*' * lenth)
    print(cytat_na_dzis)
    print('*' * lenth)


def main():
    cytat_na_dzis = losowanie()


main()
losowanie()
show(cytat_na_dzis)
