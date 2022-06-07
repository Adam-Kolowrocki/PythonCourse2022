# Napisz grę - kamień (k) / papier (p) / nożyce (n).
#         Użytkownik podaje jedną z 3 figur.
#         Komputer losuje jedną z 3 figur.
#         Sprawdź kto wygrał tę rundę.
#         Zmień kod tak, by użytkownik mógł podać liczbę rund.
#         Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#         Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random
print(f'Zagrajmy w Kamień/papier/nożyce.')
round_num = int(input(f'Ile rund chcesz rozegrać ->'))
comp_score = 0
user_score = 0
round_counter = 0

while round_counter < round_num:
    user_choice = input(f'Podaj "k" albo "p" albo "n" ->')
    comp_choice = random.choice('kpn')
    round_counter += 1
    if comp_choice == 'k' and user_choice == 'p':
        user_score += 1
    elif comp_choice == 'k' and user_choice == 'n':
        comp_score += 1
    elif comp_choice == 'k' and user_choice == 'k':
        break
    elif comp_choice == 'p' and user_choice == 'n':
        user_score += 1
    elif comp_choice == 'p' and user_choice == 'k':
        comp_score += 1
    elif comp_choice == 'p' and user_choice == 'p':
        break
    elif comp_choice == 'n' and user_choice == 'k':
        user_score += 1
    elif comp_choice == 'n' and user_choice == 'p':
        comp_score += 1
    elif comp_choice == 'n' and user_choice == 'n':
        break
print(f'Twój wynik to {user_score}, wynik komputera to {comp_score}.')
if user_score > comp_score:
    print('Wygrałeś !!!')
elif user_score == comp_score:
    print('Remis.')
else:
    print('Przegrałeś...')
