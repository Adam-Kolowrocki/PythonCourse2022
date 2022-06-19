# Oblicz średnią arytmetyczną z kilku liczb.
# Liczby będą podane przez użytkownika po przecinku.
# Napisz funkcję, która przyjmie wartości i wyświetli średnią.
# Program powinien być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

def data_collect():
    user_numbers = input(f'Podaj proszę kilka liczb całkowitych, oddzielając je przecinkami ->')
    try:
        user_numbers.isdigit()
    except ValueError:
        print(f'Błędny typ danych')
        with open('error_list.txt', 'w') as f:
            f.write(f'Wystąpił błąd {ValueError}')
            print(f'Błędny typ danych')
    user_numbers = user_numbers.split(",")
    for i in range(0, len(user_numbers)):
        user_numbers[i] = int(user_numbers[i])
    return user_numbers


def average_val():
    user_numbers = data_collect()
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
