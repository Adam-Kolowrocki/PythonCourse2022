# Dodaj menu wyboru
# Opis:
# Dodaj do obecnej gry ekran wyboru np.:
# Welcome screen:
# Welcome:
# S - Start
# P - Difficulty level
# Q - Quit
#
# End of game:
#
# Would you like to continue yes/no:

from random import choice

# wygrany: (przegrany)
WINNERS_A = {
    'k': 'n',
    'n': 'p',
    'p': 'k'
}

WINNERS_B = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES_A = ('k', 'p', 'n')
CORRECT_VALUES_B = ('k', 'p', 'n', 'j', 's')


def get_comp_choice_A():
    return choice(CORRECT_VALUES_A)


def get_comp_choice_B():
    return choice(CORRECT_VALUES_B)


def get_user_choice_A():
    while True:
        user_choice = input('Podaj wartość k - kamień, p - papier , n - nożyce: ')
        if user_choice in CORRECT_VALUES_A:
            break

    return user_choice


def get_user_choice_B():
    while True:
        user_choice = input('Podaj wartość k - kamień, p - papier , n - nożyce, s - Spock, j - jaszczurka: ')
        if user_choice in CORRECT_VALUES_B:
            break

    return user_choice


def show_result(comp, user):
    if user == comp:
        print('Remis')
    elif comp in WINNERS_B[user]:
        print('Wygrywa użytkownika')
    else:
        print('Wygrywa komputer')


def menu():
    while True:
        menu_opt = input()
        print('S - Start')
        print('P - Poziom trudności')
        print('Q - Wyjście')
        if menu_opt == 'S' or menu_opt == 'P' or menu_opt == 'Q':
            break
    return menu_opt.upper()


def level():
    while True:
        print('Gra ma dwa poziomy trudności:')
        print('A - Podstawowy')
        print('B - Wysoki')
        level_opt = input(f'Co wybierasz ->')
        if level_opt == 'A' or level_opt == 'B':
            break
    return level_opt


def level_a():
    while True:
        comp = get_comp_choice_A()
        user = get_user_choice_A()
        print(f'komputer {comp}, user {user}')
        show_result(comp, user)

        play_again = input("Czy zagrać ponownie? [T / N] -> ")
        if play_again.upper() == 'N':
            break


def level_b():
    while True:
        comp = get_comp_choice_B()
        user = get_user_choice_B()
        print(f'komputer {comp}, user {user}')
        show_result(comp, user)

        play_again = input("Czy zagrać ponownie? [T / N] -> ")
        if play_again.upper() == 'N':
            break


def main():
    while True:
        print('**** GRA K-P-N ****')
        menu()
        if menu() == 'Q':
            break
        elif menu() == 'P':
            level()
            if level() == 'A':
                level_a()
            elif level() == 'B':
                level_b()
        else:
            level_a()
            break

    print('Dzięki za grę!')


main()