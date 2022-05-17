# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie
# (np. secret_num = 5). Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
player_num = int(input('Zagrajmy w grę. Podaj liczbę całkowitą z zakresu od 0 do 20... '))

while player_num == secret_num:
    print('Nie zgadłeś !!! \nPróbuj dalej')
# print('Wspaniale!!! \nTo właśnie o', player_num, 'chodziło.')