# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

nat = int(input('Podaj liczbę naturalną z zakresu od 1 do 8:'))
i = 1
s = 1
if nat == 0:
    print('0! = 1')
elif nat == 1:
    print('1! = 1')
else:
    print(f'{nat}! =')
for n in range(1, nat):
    print(n, end=' * ')
while i <= nat:
    s *= i
    i += 1
print(nat, '=', s)
print(f'Silnia z {nat} wynosi {s}')
