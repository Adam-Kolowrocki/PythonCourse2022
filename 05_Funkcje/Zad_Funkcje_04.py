# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
# (wykorzystać funkcje z pkt 2)

def list_func(num_list):
    """This function returns sum of numbers in a list."""
    return num_list


num_list = input('Podaj listę liczb oddzielonych spacjami ->')
num_list = num_list.split()
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
result = list_func(num_list)


def is_even(result):
    """This function check is the number is even."""
    return even_list

even_list = []
for i in range(len(result)):
    if i % 2 == 0:
        even_list = result.append(i)

# result_1 = is_even(result)

print(f'Suma elementów listy {num_list} jest równa : {even_list}')
