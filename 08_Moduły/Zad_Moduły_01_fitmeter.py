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
from bmi import bmi_calc


def user_data():
    print('Witaj, to jest prosty programik do obliczania Twojego BMI.')
    print()
    masa = float(input('Podaj proszę swoją masę w kg, używając "." jako separatora: '))
    wzrost = float(input('Podaj proszę swój wzrost w metrach, używając "." jako separatora: '))
    return masa, wzrost


def user_suggestion():
    masa, wzrost = user_data()
    bmi = bmi_calc(masa, wzrost)
    if bmi < 18.5:
        with open('niedowaga.txt') as f:
            suggestion = f.readline()
            print(suggestion)
    elif 18.5 < bmi <= 25:
        with open('waga_ok.txt') as f:
            suggestion = f.readline()
            print(suggestion)
    elif 25 < bmi <= 30:
        with open('nadwaga.txt') as f:
            suggestion = f.readline()
            print(suggestion)
    elif bmi > 30:
        with open('otyłość.txt') as f:
            suggestion = f.readline()
            print(suggestion)


def main():
    user_suggestion()


if __name__ == "__main__":
    main()
