# Stwórz gre w kółko i Krzyżyk dla 2 graczy.
# Zacznij od najważniejszej części – rozgrywki, a następnie dodaj menu,
# opcje takie jak imiona graczy, pomysły własne.

from random import choice


def comp_choice():
    return choice(XO)


def get_user_choice_a():
    while True:
        user_choice = input('Jaki jest twój ruch: ')
        if user_choice == X or user_choice == O:
            break

    return user_choice


def main():
    table = []


if __name__ = "__main__"
    main()
