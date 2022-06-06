# Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej
# i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić
# dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

ciag = input('Wprowadź ciąg znaków do sprawdzenia, czy jest palindromem:')
ciag_l = ciag.lower()
ciag_n = ciag_l.replace(" ","")
print('Wprowadzony ciąg to palindrom ->', ciag_n == ciag_n[::-1])