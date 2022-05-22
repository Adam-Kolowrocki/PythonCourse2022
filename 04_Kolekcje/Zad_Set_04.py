# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#     input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#     output:
#     [4, 3, 2, 1]
#     [14, 13, 12, 11]
#     [24, 23, 22, 21]

input_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
length_3 = len(input_list) // 3
list_1 = input_list.revers(0, length_3-1)
print(list_1)