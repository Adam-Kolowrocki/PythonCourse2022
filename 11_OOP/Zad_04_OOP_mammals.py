# Pomyśl, co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki.
# Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.
class Mammals:
    def __init__(self, species, kingdom, family):
        self.species = species
        self.kingdom = kingdom
        self.family = family

    def howling(self):
        print(f'{self.species} is howling when the moon is full.')

    def running(self):
        print(f'{self.species} is running very fast and jumps.')

    def roaring(self):
        print(f'{self.species} is a king of the jungle and he is roaring loud.')


def main():
    wolf = Mammals("Wilk", "Animals", "Psowate")
    horse = Mammals("Koń", "Animals", "Koniowate")
    lion = Mammals("Lew", "Animals", "Kotowate")
    ribis = Mammals("Zebra", "Animals", "Koniowate")
    wolf.howling()
    horse.running()
    lion.roaring()
    ribis.running()


if __name__ == "__main__":
    main()
