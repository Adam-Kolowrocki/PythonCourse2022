# Dysponując listą nazwisk uczestników uporządkuj ją leksykograficznie (alfabetycznie).
# Wejście:
# W pierwszym wierszu standardowego wejścia zapisano liczbę nazwisk N(1<= N <= 200).
# W następnych N wierszach zapisano po jednym nazwisku. Nazwisko rozpoczyna wielką litera,
# jego długość nie przekracza 50 znaków, i składa się tylko z liter alfabetu angielskiego.
# Wyjście :
# W kolejnych wierszach wypisz nazwiska uczestników uporządkowane alfabetycznie.

with open('Wejscie.txt', 'r') as f:
    content = []
    content.append(f.read())
    print(content)