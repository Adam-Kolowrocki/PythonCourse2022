# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą,
# MasterCard, a może AmericanExpress.
#
# Co wiemy o numerach tych kart?
#     All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#     MasterCard numbers either start with the numbers 51 through 55 or with the numbers
#     2221 through 2720. All have 16 digits.
#     American Express card numbers start with 34 or 37 and have 15 digits.

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
