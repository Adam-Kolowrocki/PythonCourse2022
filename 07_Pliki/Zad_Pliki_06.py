# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
# Sprawdź dla każdej kart jej typ. Podziel kart do plików wg typów np.
# visa.txt, mastercard.txt, americanexpress.txt.

def input_file():
    with open('karty.txt') as fopen:
        cards = fopen.readlines()

        print(cards)


input_file()
"""
def menu():
    print(f'Rozpoznawanie rodzaju karty po numerze...')
    card_num = input(f'Podaj numer Twojej karty ->')
    first_digit = card_num[0]
    return card_num, first_digit


card_num, first_digit = menu()


def card_id(first_digit):
    if first_digit == '3' and len(card_num) == 15:
        print(f'Twoja karta to American Express')
    elif first_digit == '4' and (len(card_num) == 13 or len(card_num) == 16):
        print(f'Twoja karta to Visa')
    elif (first_digit == '2' or first_digit == '5') and len(card_num) == 16:
        print(f'Twoja karta to MasterCard')
    else:
        print(f'Twoja karta nie jest ani Visa ani MasterCard ani American Express...')
        print(f'Albo podałeś błędny numer karty...')
    return


card_id(first_digit)
"""