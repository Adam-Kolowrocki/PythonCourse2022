# Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.
import os
stat_info = os.stat('inwokacja.txt')
print(f'Plika ma rozmiar {stat_info.st_size} bajtów')
