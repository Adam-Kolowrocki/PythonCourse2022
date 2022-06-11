# Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyświetl jej indeks.
numbers = (1, 3, 4, 20, 13, 16, 9)
num = input("Podaj liczbę od 1 do 20 ->")
num = int(num)
flag = False
for i, v in enumerate(numbers):
     if int(num) == v:
         print('znalazłem, pod indexem:', i)
         flag = True
         break

if not flag:
     print('nie ma takiej liczby')

"""
if num in numbers:
    print('znalazłem, pod indexem:', numbers.index(num))
else:
    print('nie ma takie liczby')
"""