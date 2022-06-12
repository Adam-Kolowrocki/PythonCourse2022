# Gra “Kamień Papier Nożyce” - menu i poziomy trudności
from random import choice


def menu():
    print('Welcome')
    print('This is the classic game - Paper, Stone, Scissors')
    print()
    print('S - Start')
    print('D - Difficulty level')
    print('Q - Quit')
    print()
    print('Remember to use capital letters...')
    user_decision = input()
    return user_decision


def level_selection():
    print('Difficulty level:')
    print('A - Smart')
    print('B - Stupid')
    level = input()
    return level


def smart():
    print('You can chose tree options:')
    print('K - Stone')
    print('P - Paper')
    print('N - Scissors')
    user_choice = input(f'What is Your choice ->')
    comp_choice = choice('KPN')
    user_score = 0
    comp_score = 0
    draw_count = 0
    round_counter = 0
    if comp_choice == 'K' and user_choice == 'P':
        user_score += 1
    elif comp_choice == 'K' and user_choice == 'N':
        comp_score += 1
    elif comp_choice == 'K' and user_choice == 'K':
        draw_count += 1
    elif comp_choice == 'P' and user_choice == 'N':
        user_score += 1
    elif comp_choice == 'P' and user_choice == 'K':
        comp_score += 1
    elif comp_choice == 'P' and user_choice == 'P':
        draw_count += 1
    elif comp_choice == 'N' and user_choice == 'K':
        user_score += 1
    elif comp_choice == 'N' and user_choice == 'P':
        comp_score += 1
    elif comp_choice == 'N' and user_choice == 'N':
        draw_count += 1
    round_counter += 1
    return user_score, comp_score, draw_count, round_counter


def stupid():
    print('You can chose five options:')
    print('K - Stone')
    print('P - Paper')
    print('N - Scissors')
    print('J - Lizard')
    print('S - Spock')
    user_choice = input(f'What is Your choice ->')
    comp_choice = choice('KPNJS')
    user_score = 0
    comp_score = 0
    draw_count = 0
    round_counter = 0
    if comp_choice == 'K' and user_choice == 'P':
        user_score += 1
    elif comp_choice == 'K' and user_choice == 'N':
        comp_score += 1
    elif comp_choice == 'K' and user_choice == 'S':
        user_score += 1
    elif comp_choice == 'K' and user_choice == 'J':
        comp_score += 1
    elif comp_choice == 'K' and user_choice == 'K':
        draw_count += 1
    elif comp_choice == 'P' and user_choice == 'N':
        user_score += 1
    elif comp_choice == 'P' and user_choice == 'K':
        comp_score += 1
    elif comp_choice == 'P' and user_choice == 'J':
        user_score += 1
    elif comp_choice == 'P' and user_choice == 'S':
        comp_score += 1
    elif comp_choice == 'P' and user_choice == 'P':
        draw_count += 1
    elif comp_choice == 'N' and user_choice == 'K':
        user_score += 1
    elif comp_choice == 'N' and user_choice == 'P':
        comp_score += 1
    elif comp_choice == 'N' and user_choice == 'S':
        user_score += 1
    elif comp_choice == 'N' and user_choice == 'J':
        comp_score += 1
    elif comp_choice == 'N' and user_choice == 'N':
        draw_count += 1
    elif comp_choice == 'J' and user_choice == 'K':
        user_score += 1
    elif comp_choice == 'J' and user_choice == 'P':
        comp_score += 1
    elif comp_choice == 'J' and user_choice == 'N':
        user_score += 1
    elif comp_choice == 'J' and user_choice == 'S':
        comp_score += 1
    elif comp_choice == 'J' and user_choice == 'J':
        draw_count += 1
    elif comp_choice == 'S' and user_choice == 'J':
        user_score += 1
    elif comp_choice == 'S' and user_choice == 'K':
        comp_score += 1
    elif comp_choice == 'S' and user_choice == 'P':
        user_score += 1
    elif comp_choice == 'S' and user_choice == 'N':
        comp_score += 1
    elif comp_choice == 'S' and user_choice == 'S':
        draw_count += 1
    round_counter += 1
    return user_score, comp_score, draw_count, round_counter

def end():
    print('Would you like to continue Yes/No:')
    decision = input()
    if decision == 'Y':
        return yes
    elif decision == 'N':
        return no


def statistics():
    print('statistics')


def main():
    if menu() == 'D':
        level_selection()
    elif menu() == 'S':
        smart()
    elif menu() == 'Q':
        print(f'End')
        statistics()
    if level_selection() == 'A':
        smart()
    elif level_selection() == 'B':
        stupid()


main()