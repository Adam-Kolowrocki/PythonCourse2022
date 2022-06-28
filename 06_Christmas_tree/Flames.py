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


def hello():
    print(clear)
    print(f'This is a simple implementation of game called:'.center(100))
    print(f'******** FLAMES ********'.center(100))
    print('\n' * 10)
    decision = input(f'Want to play?  '
                     f'Y/N -> ')
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
    print(name_1, name_2)
    flame_string = name_1 + name_2
    print(flame_string)
    for i in range(0, len(flame_string)):
        if flame_string.find(flame_string[i]) > -1:
            flame_string.lstrip(flame_string[i])
    print(flame_string)


def main():
    if hello() == 'n':
        end()
    elif hello() == 'y':
        char_removing()
    else:
        main()


if __name__ == "__main__":
    main()
