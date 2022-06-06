# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki,
# które są na pozycjach parzystych. Wykonaj na dwa sposoby
# - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
# NIESKOŃCZONE

txt = input('Podaj dowolny ciąg znaków: ')
for index, letter in enumerate(txt):
    if index % 2 == 1:
        print(letter)

print(txt[1::2])