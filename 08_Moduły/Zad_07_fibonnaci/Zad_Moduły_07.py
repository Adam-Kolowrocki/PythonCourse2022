# Stwórz moduł, który dla dowolnej wartości "n" zwróci ciąg fibonnaciego.
# Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.
from fibonnaci import fibo


def seq(n):
    print(fibo(n))


def main():
    # Main Function
    print(f'Script returns a Fibonnati sequence for "n" given by User.')
    n = int(input(f'Give "n" -> '))
    seq(n)


if __name__ == "__main__":
    main()
