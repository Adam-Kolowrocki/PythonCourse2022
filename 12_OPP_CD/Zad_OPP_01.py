# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.
# Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.
# Utwórz obiekty klas - kot, pies i człowiek, udowodnij, że rzeczywiście korzystają z klas rodziców.
class Animals:
    def not_plants(self):
        return True


class Mammals(Animals):
    def is_lifeborn(self):
        return True

class Human(Mammals):
    def __init__(self):
        print('I am A human')


class Cat(Mammals):
    def __init__(self):
        print('meow meow')


class Dog(Mammals):
    def __init__(self):
        print('Chow Chow')


hum = Human()
print(hum.is_lifeborn())
print(hum.not_plants())
dog = Dog()
cat = Cat()
