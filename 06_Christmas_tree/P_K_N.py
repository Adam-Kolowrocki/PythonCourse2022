# Gra “Kamień Papier Nożyce” - ciąg dalszy
# Obecnie rozgrywka jest utrudniona, ponieważ musimy odświeżyć grę, po każdej zakończonej grze.
# Pozwólmy użytkownikowi kontynuować niezależnie od wybranej liczby rund.
# Dodajmy pętle while oraz słowo kluczowe break.
# Po każdej rundzie zapytajmy użytkownika, czy chce kontynuować grę:
from random import choice
print(f'Zagrajmy w Kamień/papier/nożyce.')
print('W każdej chwili możesz zakończyć grę podając hasło "koniec".')
round_num = int(input(f'Ile rund chcesz rozegrać ->'))
comp_score = 0
user_score = 0
draw_count = 0
round_counter = 0
round_counter_2 = 0
user_decision = []
while round_counter < round_num:
    user_choice = input(f'Podaj "k" albo "p" albo "n" ->')
    comp_choice = choice('kpn')
    round_counter += 1
    round_counter_2 += 1
    if user_choice == 'koniec':
        print('Zakończyłeś grę.')
        break
    elif comp_choice == 'k' and user_choice == 'p':
        user_score += 1
    elif comp_choice == 'k' and user_choice == 'n':
        comp_score += 1
    elif comp_choice == 'k' and user_choice == 'k':
        draw_count += 1
    elif comp_choice == 'p' and user_choice == 'n':
        user_score += 1
    elif comp_choice == 'p' and user_choice == 'k':
        comp_score += 1
    elif comp_choice == 'p' and user_choice == 'p':
        draw_count += 1
    elif comp_choice == 'n' and user_choice == 'k':
        user_score += 1
    elif comp_choice == 'n' and user_choice == 'p':
        comp_score += 1
    elif comp_choice == 'n' and user_choice == 'n':
        draw_count += 1
    user_decision_1 = input(f'Gramy dalej? Tak/Nie ->')
    if user_decision_1 == 'n' or user_decision_1 == 'N':
        print(f'No nie!? Tak dobrze razem się bawiliśmy! Nie odpuścisz tak łatwo! Przygotuj się na kolejną rundę!')
    if round_counter == round_num:
        user_decision = input(f'Rozegraliśmy {round_counter_2} rund, chcesz grać dalej? Tak/Nie ->')
        if user_decision == 'n' or user_decision == 'N':
            break
        elif user_decision == 't' or user_decision == 'T':
            round_counter -= 1
        else:
            print(f'Niepoprawny parametr')

print(f'Twój wynik to {user_score}, wynik komputera to {comp_score} a remisów było {draw_count}.')
if user_score > comp_score:
    print('Wygrałeś !!!')
elif user_score == comp_score:
    print('Remis.')
else:
    print('Przegrałeś...')
