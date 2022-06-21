# Napisz funkcję przeszukiwania połówkowego (binarenego),
# która przyjmuje dwa parametry - szukany element oraz listę elementów.
# Zwraca informację czy element jest obecny na liście, albo nie.

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12]
elem = 21


def search():
    data_sorted = sorted(data)
    while data_sorted[0] < data_sorted[-1]:
        index = len(data_sorted) // 2
        if data_sorted[index] == elem:
            return print(f'Element {elem} znajduje się na liście...')
        else:
            if data_sorted[index] < elem:
                data_sorted = data_sorted[index:]
            else:
                data_sorted = data_sorted[:index]


def main():
    print(f'Program do wyszukiwania połówkowego.')
    print(search())


if __name__ == "__main__":
    main()
