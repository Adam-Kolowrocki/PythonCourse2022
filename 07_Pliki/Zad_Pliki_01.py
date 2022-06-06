filename = 'inwokacja.txt'

with open(filename, 'r') as f:
  content = f.read()
  print(content)

try  # obsługa błędu którego się spodziewamy
  with open('inwokacja.txt', ) as f:
    f.read()
except FileExistsError:
  print('Ten plik już istnieje')
