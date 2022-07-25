# Stwórz gre w kółko i Krzyżyk dla 2 graczy.
# Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu,
# opcje takie jak imiona graczy, pomysły własne.
from random import choice
clear = '\n' * 20


def board():
    xo_board = [
        ['', '1', '', '2', '', '3'],
        ['A', '.', '|', '.', '|', '.'],
        ['B', '.', '|', '.', '|', '.'],
        ['C', '.', '|', '.', '|', '.']
    ]
    return xo_board


def beginning():
    print(clear)
    print(f'Lets play   "Tic Tac Toe".'.center(150))
    print('\n')
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]).center(150)
                     for row in board()]).center(150))
    print('\n')
    print(f'The game is for two players.'.center(150))
    print('\n')
    input(f'Press Enter to begin.')
    player_1, player_2 = users_names()
    print(f'Player 1 name is: {player_1}, and he/she plays "X".')
    print(f'Player 2 name is: {player_2}, and he/she plays "O".')


def users_names():
    player_1 = input(f'Type name of player one -> ')
    player_2 = input(f'Type name of player two -> ')
    return player_1, player_2


def get_user_move():
    player_1, player_2 = users_names()
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]).center(150)
                     for row in board()]).center(150))
    print(f'{player_1}, type Your move:')
    column = input(f'Type "1" or "2" or "3" ->')
    row = input(f' Type "A" or "B" or "C" -> ')
    return column, row


def main():
    beginning()
    get_user_move()


if __name__ == "__main__":
    main()
