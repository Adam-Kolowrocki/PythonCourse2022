#     Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora,
#     liczbę stron, a następnie:
#
#     Sprawdź czy tytuł i nazwisko składają się tylko z liter,
#     natomiast liczba stron jest wartością liczbową.
#
#     Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
#
#     Połącz dane w jeden ciąg book za pomocą spacji
#
#     Policz liczbę wszystkich znaków w napisie book

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
