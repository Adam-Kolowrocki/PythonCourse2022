# Utwórz dekorator @uppercase_decorator,
# który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst
# zmieniony na wielkie litery.
# Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.
import time


def uppercase_decorator(text_func):
    def upper_letter():
        text_do_zmiany = text_func()
        return text_do_zmiany.upper()

    return upper_letter


def timepassed(func):
    f_time = time.time()
    return f_time


@uppercase_decorator
def text_func():
    return 'abrakadabra to czary i magia'


def main():
    to_print = text_func()
    print(to_print)


if __name__ == "__main__":
    main()
