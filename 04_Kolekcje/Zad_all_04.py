# Utwórz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 * 10,
# wypełnioną wynikami mnożenia wiersz × kolumna.

r = int(input('Do ilu mam pomnożyć?? ->'))
for a in range(1, r+1):
    for b in range(1, r+1):
        print(a * b, end="   ")
    print()
