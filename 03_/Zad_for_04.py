# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).
# NIEZROBIONE

nat = int(input('Podaj liczbę naturalną z zakresu od 1 do 8:'))
if nat > 8:
    print('Podana wartość jest zbyt duża !!!')
else:
    print(f'{nat}!=')

    first = 1

    for n in range(1, nat):
        print(n,'*')

    for n in range(1, nat):
        first *= n
        print(first)