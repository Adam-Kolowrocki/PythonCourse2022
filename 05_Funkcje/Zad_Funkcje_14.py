# Stwórz grę wisielec “bez wisielca”.
#
#     Komputer losuje wyraz z dostępnej w programie listy wyrazów.
#     Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
#     Użykownik podaje literę.
#     Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
#             “Trafione!” oraz napis ze znanymi literami.
#     W przeciwnym wpadku pokaż komunikat:
#             “Nie trafione, spróbuj jeszcze raz!”.
#     Możesz ograniczyć liczbę prób do np. 10.
print(f'Zagrajmy w wisielca... ha ha ha')
input('Naciśnij Enter a ja wylosuję dla Ciebie słowo...')

import random

words_list = ['botswana', 'zegarek', 'multipla', 'brazylia', 'stolik', 'lampka', 'karabin',
              'soczewka', 'patelnia', 'karafka', 'maskarada', 'szarada', 'skarabeusz',
              'boberek', 'telewizor', 'storczyk', 'moskitiera', 'komputer', 'poduszeczka']

hangman_idx = random.randint(0, len(words_list) - 1)
hangman_word = list(words_list[hangman_idx])
hangman_word_len = len(hangman_word)
hiden_word = hangman_word_len * "_ "
round_counter = 0
print(f'Wylosowałem dla Ciebie słowo, które ma {hangman_word_len} liter...')
print(hiden_word)


"""
def podstawianie():
    user_lit = input('Podaj literę do sprawdzenia -> ')
    if user_lit in hangman_word:
        print(f'Bardzo dobrze, litera "{user_lit}" znajduje się w wylosowanym słowie.')
"""