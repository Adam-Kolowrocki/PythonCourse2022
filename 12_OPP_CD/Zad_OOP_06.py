# Utwórz klasę Kraj, która zawiera informację o powierzchni, ludności,
# jaki język jest urzędowy, jakie miasto jest stolicą.
# Utwórz kilka obiektów klasy Kraj, stwórz listę obiektów klasy kraj, wyświetl elementy na liście krajów.
class Country:
    def __init__(self, surface, population, language, capital):
        self.surface = surface
        self.population = population
        self.language = language
        self.capital = capital


def main():
    Poland = Country('312 696', '38 179 800', 'Polski', 'Warszawa')
    Germany = Country('357 050', '82 373 000', 'Niemiecki', 'Berlin')
    France = Country('547 026', '60 656 178', 'Francuski', 'Paryż')
    United_Kingdom = Country('244 820', '66 796 800 270', 'Angielski', 'Londyn')
    country_list = [Poland, Germany, France, United_Kingdom]
    country_list.__init__()


if __name__ == "__main__":
    main()
