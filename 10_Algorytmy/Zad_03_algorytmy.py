# Przypomnij sobie szkolny wzór na silnię.
# Zapisz funkcję silnia iteracyjnie np. pętlą for,
# a następnie analogiczną funkcję tylko, że rekurencyjnie.
# Wzór na silnię n! = 1 * 2 * 3 *...*(n-1)*n
print(f'Program oblicza silnię pętlą z wykorzystaniem iteracji i rekurencji.')
user_num = int(input(f'Podaj wartość do obliczenia silni -> '))


def silnia_for():
    s = 1
    for i in range(1, user_num + 1):
        s *= i
    return s


def silnia_while():
    i = 1
    s = 1
    while i <= user_num:
        s *= i
        i += 1
    return s


def silnia_recur(user_num):
    if user_num == 1:
        return user_num
    return user_num * silnia_recur(user_num - 1)


def main():
    print(f'Silnia pętlą "while" od {user_num} wynosi {silnia_while()}.')
    print(f'Silnie pętlą "for" od {user_num} wynosi {silnia_for()}.')
    print(f' Silnia rekurencyjnie od {user_num} wynosi {silnia_recur(user_num)}.')


if __name__ == "__main__":
    main()
