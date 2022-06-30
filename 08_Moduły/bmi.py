# Moduł do obliczania BMI.
def user_data():
    print('Witaj, to jest prosty programik do obliczania Twojego BMI.')
    print()
    masa = float(input('Podaj proszę swoją masę w kg, używając "." jako separatora: '))
    wzrost = float(input('Podaj proszę swój wzrost w metrach, używając "." jako separatora: '))
    return masa, wzrost


def bmi_calc():
    masa, wzrost = user_data()
    bmi = (masa / wzrost ** 2)
    print('Twoje BMI wynosi: ', round(bmi, 1))
    return bmi


def user_suggestion():
    bmi = bmi_calc()
    if bmi < 18.5:
        print('Twoje BMi jest zbyt małe, postaraj się jeść więcej chipsów!!!')
    elif 18.5 < bmi < 24.9:
        print('Twoje BMI jest idealne, żyj zdrowo.')
    elif bmi > 24.9:
        print('Twoje BMI jest zbyt wysokie, odstaw chipsy i piwo!!!')


def main():
    user_suggestion()


if __name__ == "__main__":
    main()
