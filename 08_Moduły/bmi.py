#obliczanie BMI podejście trzecie - trening
def bmi_calc():
    bmi = (masa / wzrost ** 2)
    print('Twoje BMI wynosi: ', round(bmi, 1))
    if bmi < 18.5:
        return niedowaga
    if bmi > 18.5 and bmi < 24.9:
        return waga_normalna
    if bmi > 24.9:
        return nadwaga
