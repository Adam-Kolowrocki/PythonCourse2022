# Napisz grę - kamień (k) / papier (p) / nożyce (n).
#         Użytkownik podaje jedną z 3 figur.
#         Komputer losuje jedną z 3 figur.
#         Sprawdź kto wygrał tę rundę.
#         Zmień kod tak, by użytkownik mógł podać liczbę rund.
#         Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#         Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’
import random
comp_choice = random.choice('kpn')
print(f'Zagrajmy w Kamień/papier/nożyce.')
user_choice = input(f'Podaj "k" albo "p" albo "n" ->')

if comp_choice == 'k' and user_choice == 'p':
    print(f'Wygrałeś.')
elif comp_choice == 'k' and user_choice == 'n':
    print(f'Przegrałeś.')
elif comp_choice == 'k' and user_choice == 'k':
    print(f'Runda remisowa.')
elif comp_choice == 'p' and user_choice == 'n':
    print(f'Wygrałeś.')
elif comp_choice == 'p' and user_choice == 'k':
    print(f'Przegrałeś.')
elif comp_choice == 'p' and user_choice == 'p':
    print(f'Runda remisowa.')
elif comp_choice == 'n' and user_choice == 'k':
    print(f'Wygrałeś.')
elif comp_choice == 'n' and user_choice == 'p':
    print(f'Przegrałeś.')
elif comp_choice == 'n' and user_choice == 'n':
    print(f'Runda remisowa.')
