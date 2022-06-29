filename = 'inwokacja.txt'

with open(filename, 'r') as f:
  content = f.read()
  print(content)

try:  # obsługa błędu, którego się spodziewamy
    with open('inwokacja.txt', 'r') as f:
        print(f)
except FileExistsError:
    print('Ten plik już istnieje')
