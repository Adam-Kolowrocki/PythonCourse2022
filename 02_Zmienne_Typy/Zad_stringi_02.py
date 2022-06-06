# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3,
# dołączając s2 w środku s1.

s1 = 'Kalambury'
s2 = 'kakofonia'
print('Zmienne wyjściowe to:', s1, 'i', s2)
id_half_s1 = len(s1) // 2
s3 = s1[0:id_half_s1] + s2 + s1[id_half_s1:]
print('Ciąg po zmianach to:', s3)
