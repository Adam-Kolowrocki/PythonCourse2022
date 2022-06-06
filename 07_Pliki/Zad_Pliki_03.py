lista = ['plecak', 'menażka', 'latarka', 'zapałki', 'papier']
# pierwsza opcja
with open('lista.txt', 'w') as f:
    for i in lista:
        f.write(i + '\n')
# druga opcja
lista_str = '\n'.join(lista)
with open('lista', 'w') as f:
    f.write(lista_str)

