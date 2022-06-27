# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
from random import choice


def comp_choice():
    comp_move = choice('prs')
    return comp_move


def user_choice():
    print(f'As always You have 3 options:')
    print(f'Type "p" for paper,'
          '"r" for rock,'
          'or "s" for scissors.\n')
    user_move = input(f'What is Your move ->')
    user_move = user_move.lower()
    if not user_move in 'prs':
        user_choice()
    else:
        return user_move


def draw():
    print(f'There was a draw...')


def user_wins():
    print(f'User wins !!!')


def comp_wins():
    print(f'You have lost...')


def score_check():
    comp_move = comp_choice()
    user_move = user_choice()
    if user_move == comp_move:
        return draw()
    elif user_move == 's' and comp_move == 'p':
        user_wins()
    elif user_move == 'p' and comp_move == 'r':
        user_wins()
    elif user_move == 'r' and comp_move == 's':
        user_wins()
    else:
        comp_wins()


def main():
    print(f'Lets play a game - Paper/Rock/Scissors.')
    input(f'Press Enter to start...')
    score_check()


if __name__ == "__main__":
    main()
