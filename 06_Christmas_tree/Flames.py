# Gra FLAMES
# FLAMES to popularna gra, której nazwa postała od akronimu:
# Friends, Lovers, Affectionate, Marriage, Enemies, Sibling.
# Choć gra nie pozwala dokładnie przewidzieć przyszłości, to może sprawdzić się jako andrzejkowa wróżba.
# Jak znaleźć naszą parę?
#  Pobierz imion dwóch osób
#  Usuń wspólne litery występujące w obu imionach.
#  Policz pozostałe litery.
#  Użyj wyniku, by znaleźć prawdziwy związek między dwoma osobami.
clear = '\n' * 25
flame = 'flame'
flame_dict = {'f': 'Friendship', 'l': 'Love', 'a': 'Affection', 'm': 'Marriage', 'e': 'Enemies'}


def hello():
    print(clear)
    print(f'This is a simple implementation of game called:'.center(100))
    print(f'******** FLAMES ********'.center(100))
    print('\n' * 10)
    decision = input(f'Want to play? Y/N -> ')
    decision = decision.lower()
    return decision


def end():
    print(f'Game over.')


def names_input():
    print(clear)
    name_1 = str(input(f'Type first name to check flames -> '))
    name_2 = str(input(f'Type second name to check flames -> '))
    return name_1, name_2


def char_removing():
    name_1, name_2 = names_input()
    flame_string = name_1 + name_2
    new_string = ""
    for i in range(0, len(flame_string)):
        if flame_string.count(flame_string[i]) == 1:
            new_string += flame_string[i]
    return len(new_string), name_1, name_2


def flame_count():
    x, name_1, name_2 = char_removing()
    z = len(flame)
    while x > z:
        x -= z
    result = flame[x - 1]
    return result, name_1, name_2


def prophecy():
    result, name_1, name_2 = flame_count()
    print(clear)
    name_1 = name_1.capitalize()
    name_2 = name_2.capitalize()
    for k, v in flame_dict.items():
        if k == result:
            print(f'The prophecy for {name_1} and {name_2} is ->  {v}')


def main():
    decision = hello()
    if decision == 'y':
        prophecy()
    elif decision == 'n':
        end()
    else:
        main()


if __name__ == "__main__":
    main()
