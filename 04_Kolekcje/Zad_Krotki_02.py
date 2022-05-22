# Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

example = ('pies', 'papuga', 'panda', 'sokolica', 'łoś', 'pies', 'papuga')

if example.count('pies') > 1:
    count_pies = example.count('pies')
    print(f' Element "pies" powtarza się {count_pies} razy.')
if example.count('papuga') > 1:
    count_papuga = example.count('papuga')
    print(f' Element "papuga" powtarza się {count_papuga} razy.')
if example.count('panda') > 1:
    count_panda = example.count('panda')
    print(f' Element "panda" powtarza się {count_panda} razy.')
if example.count('sokolica') > 1:
    count_sokolica = example.count('sokolica')
    print(f' Element "sokolica" powtarza się {count_sokolica} razy.')
if example.count('łoś') > 1:
    count_łoś = example.count('łoś')
    print(f' Element "łoś" powtarza się {count_łoś} razy.')