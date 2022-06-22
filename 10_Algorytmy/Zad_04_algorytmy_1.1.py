# Napisz funkcję przeszukiwania połówkowego (binarenego),
# która przyjmuje dwa parametry - szukany element oraz listę elementów.
# Zwraca informację czy element jest obecny na liście, albo nie.

data = [3, 15, 45, 2, 6, 12, 44, 34, 21, 56, 7, 3, 12, 18, 59, 49, 46, 58, 48, 69, 78, 56, 25, 85, 36]
elem = int(input(f'Podaj wartość do odnalezienia na liście elementów -> '))
data_sorted = sorted(data)


def search(data_sorted, elem):
    lb = 0
    ub = len(data_sorted) - 1
    while lb <= ub:
        mid_v = (lb + ub) // 2
        if data_sorted[mid_v] == elem:
            return mid_v
        else:
            if data_sorted[mid_v] < elem:
                lb = mid_v + 1
            else:
                ub = mid_v - 1
    return False


def main():
    print(f'Program do wyszukiwania połówkowego.')
    if search(data_sorted, elem):
        print(f'Element {elem} znajduje się na liście.')
    else:
        print(f'{elem} nie ma na liście.')


if __name__ == "__main__":
    main()
