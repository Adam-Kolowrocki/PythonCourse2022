# Stwórz grę inspirowaną miłosną wróżbą z czasów szkolnych. Zasady gry przedstawia to wideo.
#  Pobierz imiona zakochanych
#  Policz wystąpienia każdej z liter w obu imionach oraz słowie LOVE.
#  Redukuj liczbę elementów tablicy, dodając pierwszą i ostatnią liczbę do siebie,
#  tak długo, aż zostaną dwie cyfry.
#  Dwie ostatnie cyfry tworzą wartość procentową dopasowania pary wg. wróżby.


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
    love_number_list = list(letters.values())
    print(f'lista {love_number_list}')
    love_number_str = [str(x) for x in love_number_list]
    print(f'string {love_number_str}')
    love_number = "".join(love_number_str)
    print(f'join {love_number}')
    return love_number


def love_calc():
    love_number = love_str_num()
    cycle = 0
    while len(love_number) > 2:
        if len(love_number) % 2 == 0:
            sum = int(love_number[0]) + int(love_number[-1])
            print(f'Parzysta suma = {sum}')
            middle = len(love_number) // 2
            print(f' Parzysta środek na pozycji {middle}')
            love_number = love_number[:middle + cycle] + str(sum) + love_number[middle + cycle:]
            print(f' Parzysta love_number po wstawieniu {love_number}')
            love_number = love_number[1:-1]
            print(f'Parzysta love_number po obcięciu {love_number}')
            cycle += 1
            print(f' Parzysty cykl = {cycle}')
        elif len(love_number) % 2 != 0:
            sum = int(love_number[0]) + int(love_number[-1])
            print(f'Nieparzysta suma = {sum}')
            middle = len(love_number) // 2
            print(f'Nieparzysta środek na pozycji {middle}')
            love_number = love_number[:middle + cycle] + str(sum) + love_number[middle + cycle:]
            print(f'Nieparzysta love_number po wstawieniu {love_number}')
            love_number = love_number[1:-1]
            print(f'Nieparzysta love_number po obcięciu {love_number}')
            # cycle += 1
            print(f' Nieparzysty cykl = {cycle}')
    return love_number


def main():
    love_percent = love_calc()
    print(f'Macie {love_percent}% szansy na udaną miłość...')


if __name__ == "__main__":
    main()