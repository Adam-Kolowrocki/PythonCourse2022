# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sum_func(num_list):
    """This function returns sum of numbers in a list."""
    return sum(num_list)


num_list = input('Podaj listę liczb oddzielonych spacjami ->')
num_list = num_list.split()
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
result = sum_func(num_list)
print(f'Suma elementów listy {num_list} jest równa : {result}')
