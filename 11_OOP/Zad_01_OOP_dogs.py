# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies,
# która posiada wspomniane atrybuty oraz metodę.
#         atrybuty: imię, kolor sierści, rasę
#         metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.
class Pies:
    def __init__(self, name, color, raca):
        self.name = name
        self.color = color
        self.raca = raca

    def bark(self):
        print(f'{self.name} - Wof Wof')

    def tail_whip(self):
        return f'{self.name} whips his tail'


def main():
    burek = Pies("Burek", "white_&_black", "Berneńczyk")
    punio = Pies("Punio", "Brown", "Kundel")
    burek.bark()
    print(punio.tail_whip())


if __name__ == '__main__':
    main()
