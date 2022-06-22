# Dysponując listą nazwisk uczestników uporządkuj ją leksykograficznie (alfabetycznie).
# Wejście:
# W pierwszym wierszu standardowego wejścia zapisano liczbę nazwisk N(1<= N <= 200).
# W następnych N wierszach zapisano po jednym nazwisku. Nazwisko rozpoczyna wielką literą,
# jego długość nie przekracza 50 znaków i składa się tylko z liter alfabetu angielskiego.
# Wyjście:
# W kolejnych wierszach wypisz nazwiska uczestników uporządkowane alfabetycznie.
content = [
    10,
    'Lipski',
    'Nowak',
    'Kowal',
    'Kamysz',
    'Adamiak',
    'Wojtczak',
    'Malinowski',
    'Cybulski',
    'Arendt',
    'Mroczek'
]
sorted_content = sorted(content[1::])
for item in sorted_content:
    print(item)
