# Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory,
# pory kwitnienia, gatunki. Utwórz dowolne atrybuty i metody.
# Dodaj atrybut wspólny dla wszystkich storczyków-królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.
class Storczyki:
    def __init__(self, color, flowering, species, kingdom):
        self.color = color
        self.flowering = flowering
        self.species = species
        self.kingdom = kingdom

    def flower(self):
        print(f'{self.species} has nice white flowers...')

    def smell(self):
        print(f'{self.species} has no smell at all.')

    def watering(self):
        print(f'{self.species} says - give me some water please...')


def main():
    falenopsis = Storczyki("White", "May", "Falenopsis", "Rośliny")
    dendrobium = Storczyki("Purple", "April", "Dendrobium", "Rośliny")
    cymbidium = Storczyki("Pink", "Jun", "Cymbidium", "Rośliny")
    katleja = Storczyki("Yellow", "September", "Katleja", "Rośliny")
    falenopsis.flower()
    dendrobium.watering()
    cymbidium.smell()
    katleja.smell()


if __name__ == "__main__":
    main()
