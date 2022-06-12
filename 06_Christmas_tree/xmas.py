"""for i in range(3): # repeats 3 times
    for size in range(1, 4):
        print(size*"*")
print('--------------------------')"""


"""def print_triangle(n):
    for size in range(1, n+1):
        print(size * "*")


for i in range(2, 5):
    print_triangle(i)
print('--------------------------')"""


"""def print_segment(n):
    for size in range(1, n+1, 2):
        print((size * "*").center(n))


for i in range(3, 8, 2):
    print_segment(i)
print('---------------------------------')"""


def print_segment(n, total_width):
    for size in range(1, n+1, 2):
        print((size * "*").center(total_width))


def print_tree(size):
    for i in range(3, size+1, 2):
        print_segment(i, size)


print('Choose size of Christmas tree:')
n = int(input())
print_tree(n)
