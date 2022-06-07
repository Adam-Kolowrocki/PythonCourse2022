# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery,
# wielkie litery, cyfry i znaki specjalne.

txt = input(f'podaj jakiś ciąg znaków ->')
txt_low = []
txt_up = []
txt_dig = []
txt_spec = []

for char in txt:
    if char.islower():
        txt_low.append(char)
    elif char.isupper():
        txt_up.append(char)
    elif char.isdigit():
        txt_dig.append(char)
    else:
        txt_spec.append(char)

print(f'W ciągu "{txt}" jest {len(txt_up)} wielkich liter, {len(txt_low)} małych liter, '
      f'{len(txt_dig)} cyfr i {len(txt_spec)} znaków specjalnych')
