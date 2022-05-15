# zadanie 4
title = input('Podaj tytół książki:')
name = input('Podaj nazwisko autora:')
pages = input('Podaj liczbę stron:')

print(f'Ciąg {title} zawiera same litery ->', title.isalpha())
print(f'Ciąg {name} zawiera same litery ->', name.isalpha())
print(f'Ciąg {pages} jest wartością liczbową ->', pages.isdigit())

title_cap = title.capitalize()
name_cap = name.capitalize()

strings = [title_cap, name_cap, pages]
separator = " "
book = separator.join(strings)
print(book)

print('Liczba wszystkich znaków w ciagu wynosi: ', len(book))
