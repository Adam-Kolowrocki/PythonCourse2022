# Porównaj zachowanie discard() vs remove() dla typu set.

set = {1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24}

set.discard(5)
print(set)

set.remove(5)
print(set)

# remove zwróci błąd jeśli w secie nie ma obiektu podanegodo usunięcia a discard nie zwróci błędu