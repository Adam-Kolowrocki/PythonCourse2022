# Stwórz grę wisielec “bez wisielca”.
#  Komputer losuje wyraz z dostępnej w programie listy wyrazów.
#  Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
#  Użytkownik podaje literę.
#  Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
#          “Trafione!” oraz napis ze znanymi literami.
#  W przeciwnym wypadku pokaż komunikat:
#          “Nie trafione, spróbuj jeszcze raz!”.
#  Możesz ograniczyć liczbę prób do np. 10.

from random import choice
import sys
words_list = ['antarctic', 'clock', 'motorbike', 'motorway', 'rocket', 'furniture', 'refrigerator',
              'table', 'firearms', 'computer']
clear = '\n' * 25


def random_word():
    # Select random word from words list
    secret_word = choice(words_list)
    print(f'secret word : {secret_word}')
    return secret_word.lower()


def hidden_word():
    # Hide selected word
    secret_word = random_word()
    word = '_' * len(secret_word)
    return word, secret_word


def player_wins():
    # Shows user info that he wins
    print(clear)
    print('\n' * 10)
    print(f'****** Congratulations !!!! *******')
    print(f' ******** You have Won ********')
    sys.exit()


def game_over():
    # Just Show info that user lost
    print(clear)
    print('\n' * 10)
    print(f'Yoy were hanged !!!')
    return


def play():
    # Main play function
    word, secret_word = hidden_word()
    control_word = secret_word
    round_counter = 10
    print(clear)
    print(f'Word wof You is {len(secret_word)} long.')
    print(f'And it is looking like that:     {word}     ')
    while round_counter > 0:
        user_letter = input(f'Type a letter to check ->')
        user_letter = user_letter.lower()
        if len(user_letter) > 1:
            print(f'Too many letters... Type one -> ')
            continue
        elif len(user_letter) < 1:
            print(f'Too les letters... Type at least one ->')
            continue
        else:
            if secret_word.find(user_letter) > -1:
                print(f'You hit correctly...')
                while secret_word.find(user_letter) > -1:
                    idx = secret_word.find(user_letter)
                    word = word[:idx] + user_letter + word[idx + 1:]
                    secret_word = secret_word[:idx] + '*' + secret_word[idx + 1:]
                    if word == control_word:
                        player_wins()
                        break
                    else:
                        continue
                print(f'Now the word You are looking for looks like this  {word}')
            elif secret_word.find(user_letter) == -1:
                round_counter -= 1
                print(f'You missed... Try again.')
                print(f'Word You are looking for steel looks like this  {word}')

    game_over()


def main():
    # Main function in the program
    print(f'Lets play a game...')
    print(f'****HANGMAN****')
    print('\n')
    input(f'Press Enter to start.')
    play()


if __name__ == "__main__":
    main()
