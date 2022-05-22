#  Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia,
#  rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
#  Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np.
#  “Mój pies, rasy border collie wabi się Dyzio”.

puppet = ('pies', 'mieszaniec', 'punio')
(rodzaj, rasa, imię) = puppet
# print(rodzaj)
# print(rasa)
# print(imię)

print(f'Mój', rodzaj, 'rasy', rasa, 'wabi się', imię)