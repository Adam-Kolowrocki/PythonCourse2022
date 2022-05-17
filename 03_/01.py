x = 5
if x > 4:
    print('pierwszy if')

if x >= 3:
    print('drugi if')
elif x == 5:
    print('elif')
elif x >= 0:
    print('drugi 2')
else:
    print('else')

balance = int(input('Ile masz kasy?'))
if balance > 5:
    print('Stać cię na kawę')
else:
    print('Za mało na kawę')
