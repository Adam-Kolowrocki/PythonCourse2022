#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.

names = input('Wpisz kilka imion oddzilając je spacjami: ')
names = names.split(' ')

for name in names:
    print('Hello', name)
