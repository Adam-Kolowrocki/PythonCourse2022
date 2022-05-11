name = input("Jak Ci na imię? ")
weight = float(input("Podaj wagę w kg: "))
height = float(input("Podaj wzrost w m: "))
bmi = weight / height ** 2
print(name, "twoje BMI wynosi: ", round (bmi,2))
