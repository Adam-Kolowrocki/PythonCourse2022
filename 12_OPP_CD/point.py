class Point:
    def __init__(self, num):
        self.__street = 'Wileńska'
        self.num = num

    def getter(self): # getter
        return self.__street

    def setter(self, value): # setter
        self.__street = value


address = Point(10)
print(address.num)
print(address.getter())
address.setter('Wiatraczna')
print(address.getter())