# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów
# o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.
# Przekształć powstałą listę w set.

krot_1 = ('s', 'r', 'h', 'e', 'w', 'f', 'f')
krot_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

effect = krot_1[::2] + krot_2[1::2]
effect = list(effect)
print(effect)

result_set = set(effect)
print(result_set)