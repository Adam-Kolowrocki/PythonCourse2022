# Utwórz klasę sklep. Sklep posiada różne produkty.
# W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.
class Shop():
    def __init__(self, type, colour, size):
        self.type = type
        self.colour = colour
        self.size = size


    def show(self):
        print(self.type, self.size, self.colour)

    def try_size(self):
        print(f'Przymierzasz {self.type}')

    def buy(self):
        print(f'Kupujesz {self.type}')

    def ret_back(self):
        print(f'Zwracasz {self.type}')


spodnie = {
  'type': 'jeansy',
  'colour': 'niebieskie',
  'size': '32-34'
}
koszula = {
  'type': 'casual',
  'colour': 'różowa',
  'size': 'L-40'
}
koszulka = {
  'type': 'casual',
  'colour': 'biała',
  'size': 'L'
}


def main():




if __name__ == "__main__":
    main()