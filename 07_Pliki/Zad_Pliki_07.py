# Wisielec.
# Utwórz plik zawierający listę słów wg. kategorii np. zwierzęta, owoce etc.
# Poproś użytkownika o podanie kategorii przed rozpoczęciem gry.
# Następnie wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
# Rozgrywka powinna być maksymalnie intuicyjna.
from random import choice
import sys
clear = '\n' * 25


def menu():
    # Function menu for choosing category
    print(f'You have four categories to choose.')
    print(f'Type "Z" for Zwierzęta')
    print(f'Type "O" for Owoce')
    print(f'Type "P" for Państwa')
    print(f'Type "M" for Miasta')
    user_choice = input(f'Your choice is -> ')
    return user_choice.lower()


def list_selection():
    user_choice = menu()
    # Function returns category chosen by user from a file
    with open('wisielec_lista.txt', 'r') as f:
        if user_choice == 'z':
            words_list = f.readlines()[0]
            return words_list
        elif user_choice == 'o':
            words_list = f.readlines()[1]
            return words_list
        elif user_choice == 'p':
            words_list = f.readlines()[2]
            return words_list
        elif user_choice == 'm':
            words_list = f.readlines()[3]
            return words_list
        else:
            menu()


def random_word():
    words_list = list_selection()
    # Select random word from words list
    words_list = words_list.split(',')
    secret_word = choice(words_list)
    return secret_word.lower()


def hidden_word():
    # Hide selected word
    word = '_' * len(random_word())
    return word


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
    word = hidden_word()
    print(word)
    secret_word = random_word()
    print(secret_word)
    control_word = secret_word
    print(control_word)
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
    # list_selection(user_choice=menu())
    play()


if __name__ == "__main__":
    main()
