# Dodaj menu wyboru
# Opis:
# Dodaj do obecnej gry ekran wyboru np.:
# Welcome screen:
# Welcome:
# S - Start
# P - Difficulty level
# Q - Quit
# End of game:
# Would you like to continue yes/no:

from random import choice

# wygrany: (przegrany)
WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES = ('k', 'p', 'n', 'j', 's')


def get_comp_choice_a():
    return choice(CORRECT_VALUES[0:3])


def get_comp_choice_b():
    return choice(CORRECT_VALUES)


def get_user_choice_a():
    while True:
        user_choice = input('Podaj wartość k - kamień, p - papier , n - nożyce: ')
        if user_choice in CORRECT_VALUES[0:3]:
            break

    return user_choice


def get_user_choice_b():
    while True:
        user_choice = input('Podaj wartość k - kamień, p - papier , n - nożyce, s - Spock, j - jaszczurka: ')
        if user_choice in CORRECT_VALUES:
            break

    return user_choice


def show_result(comp, user):
    user_wins = 0
    comp_wins = 0
    draw_count = 0
    round_count = 0
    round_count += 1
    if user == comp:
        draw_count += 1
        print('Remis')
    elif comp in WINNERS[user]:
        user_wins += 1
        print('Wygrywa użytkownika')
    else:
        comp_wins += 1
        print('Wygrywa komputer')
    return round_count, user_wins, comp_wins, draw_count


def menu():
    while True:
        print('S - Start')
        print('P - Poziom trudności')
        print('Q - Wyjście')
        menu_opt = input()
        if menu_opt.upper() == 'Q':
            end()
            break
        elif menu_opt.upper() == 'P':
            level()
            break
        elif menu_opt.upper() == 'S':
            level_a()
        else:
            continue
    return


def level():
    while True:
        print('Gra ma dwa poziomy trudności:')
        print('A - Podstawowy')
        print('B - Wysoki')
        print('P - Powrót do menu głównego')
        level_opt = input(f'Co wybierasz ->')
        if level_opt.upper() == 'A':
            level_a()
        elif level_opt.upper() == 'B':
            level_b()
        elif level_opt.upper() == 'P':
            menu()
            break


def level_a():
    while True:
        comp = get_comp_choice_a()
        user = get_user_choice_a()
        print(f'komputer {comp}, user {user}')
        show_result(comp, user)

        play_again = input("Czy zagrać ponownie? [T / N] -> ")
        if play_again.upper() == 'N':
            break


def level_b():
    while True:
        comp = get_comp_choice_b()
        user = get_user_choice_b()
        print(f'komputer {comp}, user {user}')
        show_result(comp, user)

        play_again = input("Czy zagrać ponownie? [T / N] -> ")
        if play_again.upper() == 'N':
            break


def statistics():
    print(f'Rozegrałeś {round_count} rund.')
    print(f'Wygrałeś {user_wins}, co stanowi {user_wins / round_count * 100}% rozgrywek.')


def end():
    while True:
        statistics()
        print()
        print('Dzięki za grę!')
        break


def main():
    print('**** GRA K-P-N ****')
    menu()


main()
