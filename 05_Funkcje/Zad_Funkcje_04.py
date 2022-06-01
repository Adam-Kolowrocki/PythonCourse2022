# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
# (wykorzystać funkcje z pkt 2)

def list_func(num_list):
    """This function returns a list of numbers."""
    num_list = num_list.split()
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list


num_list = input('Podaj listę liczb oddzielonych spacjami ->')
list_func(num_list)
result_1 = list_func(num_list)

def is_even(result_1):
    """This function check is the numbers in a list are even."""
    even_list = []
    for i in range(len(result_1)):
        if result_1[i] % 2 == 0:
            even_list.append(result_1[i])
    return even_list


is_even(result_1)
print(f'Z elementów listy {result_1} parzyste są : {is_even(result_1)}')
