# zadanie 5
ciag = input('Wprowadź ciąg znaków do sprawdzenia, czy jest palindromem:')
ciag_l = ciag.lower()
ciag_n = ciag_l.replace(" ","")
print('Wprowadzony ciag to palindrom ->', ciag_n == ciag_n[::-1])