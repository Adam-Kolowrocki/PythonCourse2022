# Stwórz grę ciepło zimno.
#         Komputer losuje liczbę z zakresu od 1 do 100.
#         Użytkownik podaje swój traf.
#         Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#         Jeśli użytkownik zgadnie wygrywa gracz.
#         Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.
import random

print(f'Zagrajmy w Ciepło/Zimno...')
print(f'Twoje zadanie to, odgadnąć liczbę z zakresu od 1 do 100...')
print(f'Ale nie bój nic, będę Ci pomagał ;)')
input(f'Naciśnij "Enter" żeby zacząć grę')
seacret_num = random.randint(1, 100)
round_counter = 0

while round_counter < 6:
    round_counter += 1
    user_num = int(input(f'Podaj swój typ -> '))
    if seacret_num == user_num:
        print(f'Doskonale, wygrałeś za {round_counter} podejściem.')
        break
    elif user_num in range((seacret_num - 5), (seacret_num + 5)):
        print(f'Gorąco...')
    elif user_num in range((seacret_num - 15), (seacret_num + 15)):
        print('Ciepło')
    elif user_num in range((seacret_num - 25), (seacret_num + 25)):
        print('Letnio')
    elif user_num in range((seacret_num - 35), (seacret_num + 35)):
        print('Zimno')
    elif user_num in range((seacret_num - 45), (seacret_num + 45)):
        print('Lodowato')
    else:
        print(f'Biegun północny')
else:
    print(f'Przekroczona liczba rund. Przegrałeś...')
