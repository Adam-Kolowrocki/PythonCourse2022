# Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory,
# pory kwitnienia, gatunki. Utwórz dowolne atrybuty i metody.
# Dodaj atrybut wspólny dla wszystkich storczyków-królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.
class Storczyki:
    Kingdom = 'Plants'

    def __init__(self, color, flowering, species):
        self.color = color
        self.flowering = flowering
        self.species = species

    def flower(self):
        print(f'{self.species} has nice white flowers...')

    def smell(self):
        print(f'{self.species} has no smell at all.')

    def watering(self):
        print(f'{self.species} says - give me some water please...')


def main():
    falenopsis = Storczyki("White", "May", "Falenopsis")
    dendrobium = Storczyki("Purple", "April", "Dendrobium")
    cymbidium = Storczyki("Pink", "Jun", "Cymbidium")
    katleja = Storczyki("Yellow", "September", "Katleja")
    falenopsis.flower()
    dendrobium.watering()
    cymbidium.smell()
    katleja.smell()


if __name__ == "__main__":
    main()
