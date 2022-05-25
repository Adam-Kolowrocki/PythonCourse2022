# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy
# w formie tabeli n x n. Elementy powinny być oddzielone spacją
# wejście:
# n = 3
# tab = [['-', '-', '-']
#        ['-', '-', '-'],
#        ['-', '-', '-']]
# wyjście:
# - - -
# - - -
# - - -

n = int(input('Podaj liczbę od 1 do 10 ->'))
tab = [['_'] * n] * n

for row in tab:
    for i in row:
        print(i, end=' ')
    print()
