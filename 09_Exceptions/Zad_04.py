# Oblicz średnią arytmetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinien być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def data_collect():
    user_input = input(f'Podaj proszę kilka liczb całkowitych, oddzielając je przecinkami ->')
    user_input = user_input.split(",")
    return user_input


def data_check():
    user_input = data_collect()
    try:
        for i in range(len(user_input)):
            user_input[i] = int(user_input[i])
    except ValueError:
        with open('error_list.txt', 'w') as f:
            f.write(f'Wystąpił błąd "ValueError"')
            user_input.clear()
            main()
    except TypeError:
        with open('error_list.txt', 'w') as f:
            f.write(f'Wystąpił błąd "TypeError"')
            user_input.clear()
            main()
    return user_input


def average_val():
    user_numbers = data_check()
    val_sum = 0
    for i in range(0, len(user_numbers)):
        val_sum += user_numbers[i]
    average = val_sum / len(user_numbers)
    return average


def main():
    print(f'Hello')
    print(f'Will You test me ?')
    print(f'Średnia arytmetyczna z podanych liczby wynosi: {average_val()}')


if __name__ == "__main__":
    main()
