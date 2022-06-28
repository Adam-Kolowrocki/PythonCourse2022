# Stwórz gre w kółko i Krzyżyk dla 2 graczy.
# Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu,
# opcje takie jak imiona graczy, pomysły własne.
from random import choice
clear = '\n' * 25


def beginning():
    print(clear)
    print('\n' * 5)
    xo_board = [
        ['', '1', '2', '3'],
        ['A', '.', '.', '.'],
        ['B', '.', '.', '.'],
        ['C', '.', '.', '.']
    ]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]).center(150)
                     for row in xo_board]).center(150))
    print('\n' * 5)
    print(f'Lets play   "Tic Tac Toe"'.center(150))


def comp_choice():
    return choice(XO)


def get_user_choice_a():
    while True:
        user_choice = input('Jaki jest twój ruch: ')
        if user_choice == X or user_choice == O:
            break

    return user_choice


def main():
    beginning()


if __name__ == "__main__":
    main()
