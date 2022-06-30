with open('shakespeare.txt', 'w') as fopen:
    message = 'Be or Not To Be'
    print(message)  # wyświetli na standardowe wyjście
    print(message, file = fopen) # zapis do pliku
    # Można ustawić zarówno parametr file i wyświetlić wartość na ekranie
    # potrzebujemy przekazać wartość None, bezpośrednio lub za pomocą zmiennej
    nofile = None
    print(message, file = nofile)  # wyświetli na standardowe wyjście
    print(message, file = None)


cytaty_3 = []
print(type(cytaty_3))


card_num = '312548963251456'
first_digit = '3'
if first_digit == '3' and len(card_num) == 15:
    print('is visa')

with open('wisielec_lista.txt', 'r') as f:
    user_choice = input(f'podaj wybór')
    if user_choice == 'z':
        words_list = f.readlines()[0]
        print(words_list)
    elif user_choice == 'o':
        words_list = f.readlines()[1]
        print(words_list)
    elif user_choice == 'p':
        words_list = f.readlines()[2]
        print(words_list)
    elif user_choice == 'm':
        words_list = f.readlines()[3]
        print(words_list)
    else:
        print(f'wrong choice')
