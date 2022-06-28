def names_input():

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
    return len(new_string)


def main():
    print(char_removing())


if __name__ == "__main__":
    main()
