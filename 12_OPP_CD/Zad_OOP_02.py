# Do klasy człowiek dodaj metodę super() tak,
# aby móc wyświetlić opis dostępny gdziekolwiek w klasie ssaki.
class Animals:
    def not_plants(self):
        return True


class Mammals(Animals):
    def __init__(self, classname):
        print(classname, 'UpperClass')

    def is_lifeborn(self):
        return True


class Human(Mammals):
    def __init__(self, surname):
        print(surname, 'I am A human')
        super().__init__(surname)


class Cat(Mammals):
    def __init__(self):
        print('meow meow')


class Dog(Mammals):
    def __init__(self):
        print('Chow Chow')


hum = Human(Mammals)
print(hum.is_lifeborn())
print(hum.not_plants())
