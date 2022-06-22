# Write a function called FooBar that takes input integer n and prints all the numbers
# from 1 upto n in a new line. If the number is divisible by 3 then print "Foo",
# if the number is divisible by 5 then print "Bar" and if the number is divisible by both 3 and 5,
# print "FooBar". Otherwise just print the number.
def data_collect():
    print(f'Funkcja "FooBar"')
    user_num = int(input(f'Podaj liczbę całkowitą dla której mam przeprowadzić "FooBar"'))
    return user_num


def foo_bar():
    user_num = data_collect()
    for n in range(1, user_num + 1):
        if n % 3 == 0 and n % 5 == 0:
            print(f'FooBar')
        elif n % 3 == 0:
            print(f'Foo')
        elif n % 5 == 0:
            print(f'Bar')
        else:
            print(n)


def main():
    foo_bar()


if __name__ == "__main__":
    main()
