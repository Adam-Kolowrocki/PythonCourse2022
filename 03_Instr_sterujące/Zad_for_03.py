# Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
# Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

sum_numbers = 0
for num in range(1, 11):
    sum_numbers += num # sum_numbers = sum_numbers + num
    print(sum_numbers)
    