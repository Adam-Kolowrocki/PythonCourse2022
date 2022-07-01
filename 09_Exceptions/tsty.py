import sys

try:
    my_function()
except Exception:
    print("Błąd to: ", sys.exc_info()[0])

print('Początek programu')
raise Exception('To jest ogólny wyjątek')
print('Koniec programu')
