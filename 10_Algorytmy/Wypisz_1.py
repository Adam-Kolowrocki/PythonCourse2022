def wypisz(n):
    if(n < 0):  # (1)
        print("-")
        n = -n
    if(n / 10 != 0):  # (2)
        wypisz(n / 10)
    print("%d", (n % 10)) # (3)

wypisz(123)