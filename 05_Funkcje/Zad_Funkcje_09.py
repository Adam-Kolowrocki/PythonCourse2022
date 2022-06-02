# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
secret_num = 56
clear = "\n" * 50


def hello():
    print(f'Lets play a game ;) -> Ciepło - zimno')
    print()
    print(f'Odgadnij tajną liczbę z zakresu 0-100, a ja będę Ci podpowiadał...')
    input('Naciśnij Enter aby rozpocząć grę...')
    print(clear)
    return


hello()


def game():
    counter = 0
    player_num = 0
    while player_num != secret_num:
        counter += 1
        player_num = int(input(f'Podaj Twój typ ?'))
        if player_num == secret_num:
            print(f'Gratulacje, odgadłeś tajną liczbę za {counter} razem !!!')
        elif player_num != secret_num and ((secret_num - 5) < player_num < (secret_num + 5)):
            print(f'Parzy !!!')
        elif (secret_num - 10) < player_num <= (secret_num - 5) or (secret_num + 5) <= player_num < (secret_num + 10):
            print(f'Gorąco !!!')
        elif (secret_num - 15) < player_num <= (secret_num - 10) or (secret_num + 10) <= player_num < (secret_num + 15):
            print(f'Ciepło !!!')
        elif (secret_num - 20) < player_num <= (secret_num - 15) or (secret_num + 15) <= player_num < (secret_num + 20):
            print(f'Ledwie letnio !!!')
        elif (secret_num - 25) < player_num <= (secret_num - 20) or (secret_num + 20) <= player_num < (secret_num + 25):
            print(f'Zimno !!!')
        elif (secret_num - 35) < player_num <= (secret_num - 25) or (secret_num + 25) <= player_num < (secret_num + 35):
            print(f'Lodowato !!!')
        elif player_num <= (secret_num - 35) or (secret_num + 35) <= player_num:
            print(f'Jesteś tak daleko, że piekło zamarza!!!')
    return


game()
