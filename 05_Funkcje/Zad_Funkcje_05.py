# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi
# na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

print('Witaj, to jest prosty programik do obliczania Twojego BMI.')
print()

def bmi_calc():
    masa = float(input('Podaj proszę swoją masę w kg, używając "." jako separatora: '))
    wzrost = float(input('Podaj proszę swój wzrost w metrach, używając "." jako separatora: '))
    bmi = (masa / wzrost ** 2)
    return bmi


bmi = bmi_calc()


def result(bmi):
    print('Twoje BMI wynosi: ', round(bmi, 1))
    if bmi < 18.5:
            print('Twoje BMi jest zbyt małe, postaraj się jeść więcej chipsów!!!')
    if bmi > 18.5 and bmi < 24.9:
        print('Twoje BMI jest idealne, żyj zdrowo.')
    if bmi > 24.9:
        print('Twoje BMI jest zbyt wysokie, odstaw chipsy i piwo!!!')


result(bmi)
