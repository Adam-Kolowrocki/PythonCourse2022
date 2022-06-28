# Stwórz gre w kółko i Krzyżyk dla 2 graczy.
# Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu,
# opcje takie jak imiona graczy, pomysły własne.
from random import choice
clear = '\n' * 25


def board():
    xo_board = [
        ['', '1', '2', '3'],
        ['A', '.', '.', '.'],
        ['B', '.', '.', '.'],
        ['C', '.', '.', '.']
    ]
    return xo_board


def beginning():
    print(clear)
    print('\n' * 5)
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]).center(150)
                     for row in board()]).center(150))
    print('\n' * 5)
    print(f'Lets play   "Tic Tac Toe".'.center(150))
    print('\n')
    print(f'The game is for two players.'.center(150))
    print('\n')
    input(f'Press Enter to begin.')


def users_names():
    player_1 = input(f'Type name of player one -> ')
    player_2 = input(f'Type name of player two -> ')
    return player_1, player_2


def instruction():
    print(clear)
    print(f'Player One starts by choosing the sign - "X" or "O"')
    print(f'You can use lowercase or uppercase.')
    print(f'Then You are pointing a place to put Your move,')
    print(f'by typing "1","2" or "3" for column and "A","B" or "C" for row.')


def get_user_choice(player_1):
    while True:
        user_choice = input(f'{player_1}, what is your choice? ("X/O") -> ')
        if user_choice == X or user_choice == O:
            break
    return user_choice


def get_user_move():
    column = input(f'Type "1" or "2" or "3" ->')
    row = input(f' Type "A" or "B" or "C" -> ')
    return column, row


def main():
    beginning()
    instruction()


if __name__ == "__main__":
    main()

    # xo_board[1][1] = 'X'
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]).center(150)
    #                  for row in xo_board]).center(150))
