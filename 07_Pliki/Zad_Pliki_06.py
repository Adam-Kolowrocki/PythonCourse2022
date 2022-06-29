# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
# Sprawdź dla każdej kart jej typ. Podziel karty do plików wg typów np.
# visa.txt, mastercard.txt, americanexpress.txt.
def input_file():
    with open('karty.txt') as fopen:
        cards = fopen.readlines()
    return cards


def card_id(cards):
    for i in range(0, len(cards)):
        card_num = cards[i].strip('\n')
        first_digit = card_num[0]
        if first_digit == '3' and len(card_num) == 15:
            with open('americanexpress.txt', 'a') as f:
                f.write(f'Numer karty AmericanExpress: \n')
                f.write(card_num)
                f.write('\n')
        elif first_digit == '4' and (len(card_num) == 13 or len(card_num) == 16):
            with open('visa.txt', 'a') as f:
                f.write(f'Numer karty Visa: \n')
                f.write(card_num)
                f.write('\n')
        elif (first_digit == '2' or first_digit == '5') and len(card_num) == 16:
            with open('mastercard.txt', 'a') as f:
                f.write(f'Numer karty MasterCard: \n')
                f.write(card_num)
                f.write('\n')
        else:
            with open('others_errors.txt', 'a') as f:
                f.write(f'Numer karty nieznanego wystawcy lub błędny: \n')
                f.write(card_num)
                f.write('\n')


def main():
    print(f'Rozpoznawanie rodzaju karty na podstawie numerów pobranych z pliku...')
    card_id(cards=input_file())


if __name__ == "__main__":
    main()



