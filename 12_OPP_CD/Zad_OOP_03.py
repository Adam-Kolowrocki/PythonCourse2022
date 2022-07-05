#  Zadanie inspirowane popkulturą: https://www.youtube.com/watch?v=Ct6BUPvE2sM
# Stwórz klasę PenPinapple, która dziedziczy z klas Pen oraz Pinapple.
# Logiki to nie ma, więc dodaj wg uznania.
class Pen:
    def write_with_inc(self):
        print(f'Pen is an item to write things...')


class Pinapple:
    def sweet_fruit(self):
        print(f'It is a sweet fruit with leafs...')


class PenPinapple(Pen, Pinapple):
    def __init__(self):
        print(f'This is PenPinapple...')


def main():
    fruit = PenPinapple()
    fruit.write_with_inc()
    fruit.sweet_fruit()


if __name__ == "__main__":
    main()
