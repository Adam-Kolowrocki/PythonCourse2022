# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies,
# która posiada wspomniane atrybuty oraz metodę.
#         atrybuty: imię, kolor sierści, rasę
#         metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.
dyzio = {
  'imię': 'Dyzio',
  'kolor_sierści': 'biała',
  'rasa': 'Coton de Tulear'
}


class Pies():
    def __init__(self, imię, kolor_sierści, rasa):
        self.imię = imię
        self.kolor_sierści = kolor_sierści
        self.rasa = rasa

    def chow(self):
        print(f'{self.imię} - How How')

    def machaj(self):
        return f'{self.imię}' Macha Ogonem

