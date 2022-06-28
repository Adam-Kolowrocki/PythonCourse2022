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
    love_number_str = [str(x) for x in love_number_list]
    love_number = "".join(love_number_str)
    return love_number


def love_calc():
    love_number = love_str_num()
    cycle = 0
    new_love_number = ""
    while len(love_number) > 1:
        if len(love_number) % 2 == 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            love_number = love_number[1:-1]
            cycle += 1
        elif len(love_number) % 2 != 0:\
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            love_number = love_number[1:-1]
            new_love_number += love_number
        print(f'New love number po pierwszej pętli while {new_love_number}')
    return new_love_number



"""def love_calc():
    love_number = love_str_num()
    cycle = 0
    new_love_number = ""
    while len(love_number) > 1:
        if len(love_number) % 2 == 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
            cycle += 1
        elif len(love_number) % 2 != 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
    new_love_number += love_number
    print(f'New love number po pierwszej pętli while {new_love_number}')
    love_number = new_love_number
    cycle = 0
    new_love_number = ""
    while len(love_number) > 1:
        if len(love_number) % 2 == 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
            cycle += 1
        elif len(love_number) % 2 != 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
    new_love_number += love_number
    print(f'New love number po drugiej pętli while {new_love_number}')
    love_number = new_love_number
    cycle = 0
    new_love_number = ""
    while len(love_number) > 1:
        if len(love_number) % 2 == 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
            cycle += 1
        elif len(love_number) % 2 != 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
    new_love_number += love_number
    print(f'New love number po trzeciej pętli while {new_love_number}')
    love_number = new_love_number
    cycle = 0
    new_love_number = ""
    while len(love_number) > 1:
        if len(love_number) % 2 == 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
            cycle += 1
        elif len(love_number) % 2 != 0:
            sum = int(love_number[0]) + int(love_number[-1])
            sum = str(sum)
            new_love_number += sum
            print(new_love_number)
            love_number = love_number[1:-1]
    new_love_number += love_number
    print(f'New love number po czwartej pętli while {new_love_number}')
    return new_love_number
"""


def main():
    love_percent = love_calc()
    print(f'Macie {love_percent}% szansy na udaną miłość...')


if __name__ == "__main__":
    main()