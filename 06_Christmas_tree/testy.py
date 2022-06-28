xo_board = [
    ['', '1', '2', '3'],
    ['A', '.', '.', '.'],
    ['B', '.', '.', '.'],
    ['C', '.', '.', '.']
]
print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in xo_board]))
#
# for row in xo_board:
#     for index, value in enumerate(row):
#         if index == 1:
#             print(value, end=" | ")
#         else:
#             print(value, end=" ")
#
# ----------------------------------------------------------------------------------
# def names_input():
#
#     name_1 = str(input(f'Type first name to check flames -> '))
#     name_2 = str(input(f'Type second name to check flames -> '))
#     return name_1, name_2
#
#
# def char_removing():
#     name_1, name_2 = names_input()
#     flame_string = name_1 + name_2
#     new_string = ""
#     for i in range(0, len(flame_string)):
#         if flame_string.count(flame_string[i]) == 1:
#             new_string += flame_string[i]
#     return len(new_string)
#
#
# def main():
#     print(char_removing())
#
#
# if __name__ == "__main__":
#     main()
