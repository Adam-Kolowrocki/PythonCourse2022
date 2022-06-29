# Wyświetl tylko 5 pierwszych linii
with open('inwokacja.txt') as file:
    lines = file.readlines()
    for l in range(0, 5):
        print('Line ' + str(l + 1) + ' : ' + lines[l])
