# Stwórz grę inspirowaną miłosną wróżbą z czasów szkolnych. Zasady gry przedstawia to wideo.
#     Pobierz imiona zakochanych
#     Policz wystąpienia każdej z liter w obu imionach oraz słowie LOVE.
#     Redukuj liczbę elementów tablicy dodając pierwszą i ostatnią liczbę do siebie,
#     tak długo, aż zostną dwie cyfry.
#     Dwie ostatnie cyfry tworzą wartość procentową dopasowania pary wg. wróżby.


def name_collect():
    print(f'Program oblicza % szansy na udaną miłość na podstawie bardzo zaawansowanego algorytmu, '
          f'który bierze pod uwagę całą masę zmiennych ;)')
    name_1 = input(f'Podaj swoje imię ->')
    name_2 = input(f'Podaj imię Twojej miłości ->')
    love_string = name_1.lower() + 'loves' + name_2.lower()
    return love_string


def love_str_num():
    love_string = name_collect()
    letters = {}
    for char in love_string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    love_number = list(letters.values())
    return love_number


def love_calc():
    love_num = love_str_num()
    while len(love_num) > 2:
        if len(love_num) % 2 == 0:
            sum = love_num[0] + love_num[-1]
            del love_num[0]
            del love_num[-1]
            love_num.insert(int(len(love_num) // 2), sum)
        elif len(love_num) % 2 != 0:
            sum = love_num[0] + love_num[-1]
            del love_num[0]
            del love_num[-1]
            love_num.insert(((len(love_num) // 2) + 1), sum)
    return love_num


def main():
    love_percent = love_calc()
    to_print = str(love_percent[0]) + str(love_percent[1])
    print(f'Macie {to_print}% szansy na udaną miłość...')


if __name__ == "__main__":
    main()