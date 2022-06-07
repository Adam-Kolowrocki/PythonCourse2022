txt = input('Podaj jakiś ciąg: ')

counter_num = 0
counter_up = 0
counter_low = 0
for letter in txt:
    print(letter)
    if letter.isdigit():
        counter_num += 1

    if letter.isupper():
        counter_up += 1

    if letter.islower():
        counter_low += 1

print(f'Text: {txt}')
print('Cyfry', counter_num)
print('Wielkie', counter_up)
print('Małe', counter_low)