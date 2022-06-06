# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

wyraz = 'Warszawskiego'
print('Ciąg wyjściowy to:', wyraz)
id_half = len(wyraz) // 2
print('Ciąg złożony z trzech środkowych znaków wyrazu "', wyraz, '" to: "', wyraz[id_half-1:id_half+2], '"')
