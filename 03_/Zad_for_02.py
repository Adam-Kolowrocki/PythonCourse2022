# Utwórz listę, która zawiera składniki na ulubione danie.
# Wyświetl komunikaty co należy pokolei dodać.
# Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

ingredients = ['egg whites', 'shugar', 'egg yolks', 'flour', 'evaporated milk', 'milk']
step_1 = "Ubij na sztywną pianę"
step_2 = "dalej ubijaj"
step_3 = "dodawaj małymi porcjami, nie ubijaj, mieszaj szpatułką,"
step_4 = "przelej do foremki i wstaw do piekarnika na 180 st. na 25 min"
step_5 = "ciasto wystudź, nakłuj wykałaczką i zalej zmieszanym mlekiem"

for i in ingredients:
    print('-', i)
    if i == 'egg whites':
        print(step_1)
    if i == 'shugar':
        print(step_2)
    if i == 'egg yolks':
        print(step_2)
    if i == 'flour':
        print(step_3, step_4)
    if i == 'milk':
        print(step_5)
