# Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py.
# Zaimportuj moduł do pliku fitmeter.py. Nowy plik będzie informował użytkownika o jego aktualnym BMI
# i na podstawie wyniku (niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.
#
#  Utwórz plik bmi.py zawierający metodę obliczania bmi.
#  Metoda zwraca wartości: niedowaga, waga normalna, nadwaga, otyłość.
#  Utwórz 4 pliki .txt zawierające porady.
#  Utwórz plik fitmeter.py, który zaimportuje moduł bmi.
#  fitmeter.py pobierze wagę i wzrost pacjenta i przekaże do odpowiedniej funkcji z modułu bmi.
#  Na podstawie zwróconej wartości fitmeter.py wyświetli odpowiednie porady dla pacjenta.
import bmi

print('Witaj, to jest prosty programik do obliczania Twojego BMI.')
print()
masa = float(input('Podaj proszę swoją masę w kg, używając "." jako separatora: '))
wzrost = float(input('Podaj proszę swój wzrost w metrach, używając "." jako separatora: '))

if