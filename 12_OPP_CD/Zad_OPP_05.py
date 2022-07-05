# Stwórz abstrakcyjną klasę Pojazdy. Utwórz potomne klasy pojazdy np.
# Samochód, Rower, Autobus, Ciężarówki. Dodaj opisy zgodne z tym,
# jak te pojazdy są klasyfikowane. Jaki rodzaj dokumentu jest potrzebny,
# by kierować poszczególnym pojazdem.

from abc import ABC, abstractmethod


class Pojazdy(ABC):  #klasa abstrakcyjna
    @abstractmethod
    def opis(self):
        pass

    @abstractmethod
    def uprawnienia(self):
        pass


class Samochod(Pojazdy):
    def __init__(self):
        return 'silnik'

    def dokument(self):
        return 'Prawo_jazdy B'


class Rower(Pojazdy):
    def naped(self):
        return 'miesnie'

    def dokument(self):
        return 'karta rowerowa'


class Autobus(Pojazdy):
    def naped(self):
        return 'duży silnik'

    def dokument(self):
        return 'Prawo_jazdy D'


class Ciezarowki(Pojazdy):
    def naped(self):
        return 'duży silnik'

    def dokument(self):
        return 'Prawo_jazdy C'


def main():
    s = Samochod
    r = Rower
    a = Autobus
    c = Ciezarowki


if __name__ == "__main__":
    main()
