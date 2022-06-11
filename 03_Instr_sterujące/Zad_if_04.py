#Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string
# jest dłuższy niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera,
# wszystkie litery a podmień na z i wyświetl powstały napis.

var_str = input('Podaj dowolny ciąg znaków:')

if len(var_str) > 5:
    if "a" in var_str:
        print(var_str.replace("a","z"))
    else:
        print('Ciąg nie jest dłuższy niz 5 znaków...')