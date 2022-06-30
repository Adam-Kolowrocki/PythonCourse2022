import os

filename = 'Zad_01_fitmeter/niedowaga.txt'
if os.path.isfile(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print('Nie ma takiego pliku')
