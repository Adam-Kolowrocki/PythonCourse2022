
even_list = []
num_list = input('Podaj listę liczb oddzielonych spacjami ->')
num_list = num_list.split()
for i in range(len(num_list)):
    if v % 2 == 0:
        print(v)
      #  even_list = num_list.append(i)

# print(even_list)


def numbers():
    numbers_list = input(f'Podaj 3 liczby oddzielajac je spacjami ->')
    numbers_list = numbers_list.split()
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    return numbers_list


numbers_list = numbers()


def minimum_of(numbers_list):


