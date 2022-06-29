with open('inwokacja.txt') as fopen:
    for line in fopen:
        print(line)
print('------------------------------------------------------------')
with open('inwokacja.txt') as fopen_1:
    content = fopen_1.read()
    print(content)

print('******************************************************************')
with open('inwokacja.txt') as fopen_2:
    while True:
        current_line = fopen_2.readline()
        if current_line == "":
            break
        print(current_line)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
with open('inwokacja.txt', 'r') as fopen_3:
    lines = fopen_3.readlines()

for l in range(len(lines)):
    print("Line " + str(l), lines[l])
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
with open('inwokacja.txt') as fopen_4:
    lines = fopen_4.readlines()

for l in lines:
    print("Line : " + l)

print('####################################################################')
with open('inwokacja.txt', 'r', encoding='cp1252') as fopen_5:
    content = fopen_5.read()
print(content)

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
with open('inwokacja.txt', 'r', encoding='utf-8') as fopen_6:
    content = fopen_6.read()
print(content)

