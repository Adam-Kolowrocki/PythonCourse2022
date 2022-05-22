# Pobierz od użytkownika parzystą listę elementów.
# Sprawdź czy 2 środkowe elementy są takie same.

elements = input('Podaj parzystą listę elementów oddzielonych spacją ->')
elements = elements.split()
print(elements)
half = len(elements) // 2
print('Czy dwa środkowe elementy', elements[half-1], ' i ', elements[half], ' sa takie same ->', elements[half-1] == elements[half])