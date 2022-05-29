# Usuń duplikat z podanej list i utwórz na jej bazie krotkę.
# Znajdź minimalną i maksymalną liczbę w krotce.
#
example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]
print(f'Lista wyjściowa = {example_list}')
example_tuple = tuple(set(example_list))
print(f'Krotka bez duplikatów = {example_tuple}')

sorted_tuple = list(sorted(example_tuple))
print(f'Minimalna wartość w krotce wynosi -> {sorted_tuple[0]}')
print(f'Maksymalna wartość w krotce wynosi -> {sorted_tuple[-1]}')
