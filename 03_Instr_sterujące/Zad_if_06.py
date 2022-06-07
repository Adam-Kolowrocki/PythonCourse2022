# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę
# ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.
import random
user_num = int(input('Podaj liczbę całkowitą z zakreso od 1 do 100: '))
prog_num = random.randint(1, 100)

if user_num == prog_num:
    print('Gratulacje !!!')
else:
    print('Pudło !!!')