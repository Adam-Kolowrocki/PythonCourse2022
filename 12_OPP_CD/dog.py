class Canis:
    paws = 4

    def __init__(self):
        print('Canis is an animal')

    def show(self):
        print('🐕 🐕 🐕 🐕 🐕 🐕 🐕 🐕')


    def extra(self):
        print(f'Extra z Canis')

class Dog(Canis):
    kingdom = 'Animals'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self, sound):
        print(sound * self.age)

    def show(self):
        super().show()
        txt = f'My dog {self.name}, age: {self.age} is breed {self.breed}'
        print(txt)

    def extra(self):
        print(f'Extra z Dog')


class Fox(Canis):
    def __init__(self):
        print('create fox')



dyzio = Dog('Dyzio', 3, 'mops')
dyzio.bark('hauu')
print(dyzio.name)
print(dyzio.paws)
print(dyzio.show())

print('------------')
good_doggo = Canis()
good_doggo.show()
print('------------')
fox = Fox()
fox.show()

print(f'*************')
dyzio.extra()


print(f'//////////////////')
dyzio. # gdzieś tu powinno być upper i przeəscie do dziedizczenia wyżej
