from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def poop(self):
        pass


class Horse(Animal):

    def poop(self):
        print("Poop poop")

    def fly(self):
        print("Horse can't fly")


class Unicorn(Animal):

    def poop(self):
        print("Rainboooowww")

    def fly(self):
        print("Unicorn can fly with magical power")


class Cat(Animal):
    def meow(self):
        return 'meow meow'

    def poop(self):
        print(f'Idę do kuwety')


def family_test(self, animal):
    animal.poop(self)


arrow = Horse()
cute = Unicorn()
kity = Cat()

family_test(arrow)
family_test(cute)
family_test(Cat)
