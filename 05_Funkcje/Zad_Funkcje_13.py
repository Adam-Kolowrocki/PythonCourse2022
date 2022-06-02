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

import random

words_list = ['botswana', 'zegarek', 'multipla', 'brazylia', 'stolik', 'lampka', 'karabin',
              'soczewka', 'patelnia', 'karafka', 'maskarada', 'szarada', 'skarabeusz',
              'boberek', 'telewizor', 'storczyk', 'moskitiera', 'komputer', 'poduszeczka']

hangman_idx = random.randint(0, len(words_list) - 1)
print(hangman_idx)
# hangman_word = []
# hangman_word.append(words_list[hangman_idx])
# hangman_word = str.words_list[hangman_idx]
# print(hangman_word)
# hangman_hiden = []
