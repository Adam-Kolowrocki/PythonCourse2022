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
    input(f'Press Enter to begin...')
    names_input()


def names_input():
    print(clear)
    name_1 = input(f'Type a first name -> ')
    name_2 = input(f'Type a second name -> ')
    return name_1, name_2



    # def input_first():
    #     print(f'jestem w input_first')
    #     name_1 = input(f'Type a first name -> ')
    #     if not name_1.isalpha():
    #         print(f'Name has to be alphabetic...')
    #         input_first()
    #         return name_1
    #
    # def input_second():
    #     name_2 = input(f'Type a second name -> ')
    #     if not name_2.isalpha():
    #         print(f'Name has to be alphabetic...')
    #         input_second()
    #         return name_2
    # name_1 = input_first()
    # name_2 = input_second()
    # print(name_1, name_2)
    # return name_1, name_2



def main():
    hello()


if __name__ == "__main__":
    main()
