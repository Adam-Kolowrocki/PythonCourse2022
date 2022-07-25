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


def users_names():
    player_1 = input(f'Type name of player one -> ')
    player_2 = input(f'Type name of player two -> ')
    print(f'Player 1 name is: {player_1}, and he/she plays "X".')
    print(f'Player 2 name is: {player_2}, and he/she plays "O".')
    return player_1, player_2


def get_user_move():
    player_1, player_2 = users_names()
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]).center(150)
                     for row in board()]).center(150))
    print(f'To make Your move, type row and column, ex: "A1".')
    print(f'You can use small or capital letters...')
    player_1_move = input(f'{player_1}, type Your move:')
    column = player_1_move[:1]
    row = player_1_move[1]
    return column, row


def main():
    beginning()
    get_user_move()


if __name__ == "__main__":
    main()
