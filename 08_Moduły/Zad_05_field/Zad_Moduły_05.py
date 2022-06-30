# Stwórz moduł obliczający pola różnych figur. W nowym pliku utwórz skrypt,
# który na podstawie podanych składowych kształtów pomieszczeń oraz ich wymiarów
# zwraca powierzchnię budynku.
from fields import square, rectangle, triangle, circle, trapeze, diamond
clear = '\n' * 25


def rooms_shape():
    # Function collects numbers of rooms in different shapes
    print(clear)
    square_count = int(input(f'How many square-shape rooms is in this buildings -> '))
    rectangle_count = int(input(f'How many rectangle-shape rooms is in this buildings -> '))
    triangle_count = int(input(f'How many triangle-shape rooms is in this buildings -> '))
    circle_count = int(input(f'How many circle-shape rooms is in this buildings -> '))
    # trapeze_count = int(input(f'How many trapezoid-shape rooms is in this buildings -> '))
    # diamond_count = int(input(f'How many diamond-shape rooms is in this buildings -> '))
    return square_count, rectangle_count, triangle_count, circle_count  #, trapeze_count, diamond_count


def rooms_count():
    # Functions collect number of rooms in shapes given by user
    square_count, rectangle_count, triangle_count, circle_count = rooms_shape()
    while True:
        if square_count > 0:
            sq_a = []
            for i in range(1, square_count):
                sq_a[i] = int(input(f'Give a length of the {i} square room ->'))
            return sq_a
        if rectangle_count > 0:
            rec_a = []
            rec_b = []
            for i in range(1, rectangle_count):
                rec_a[i] = int(input(f'Give a length of the {i} rectangle room ->'))
                rec_b[i] = int(input(f'Give a width of the {i} rectangle room ->'))
            return rec_a, rec_b
        if triangle_count > 0:
            tri_a = []
            tri_h = []
            for i in range(1, rectangle_count):
                tri_a[i] = int(input(f'Give an "a" dimension of the {i} triangle room ->'))
                tri_h[i] = int(input(f'Give a "h" dimension of the {i} triangle room ->'))
            return tri_a, tri_h
        if circle_count > 0:
            cir_r = []
            for i in range(1, rectangle_count):
                cir_r[i] = int(input(f'Give a radius of the {i} circle room ->'))
            return cir_r


def main():
    # main function
    print(f'Script returns filed of the building with given shapes and dimensions.')
    print(f'There are different shapes to chose: '
          f'square, rectangle, triangle and circle.')
    input(f'Press Enter to start.')
    rooms_count()


if __name__ == "__main__":
    main()
