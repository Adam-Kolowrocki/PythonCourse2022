# Stwórz listę pomysłów na prezent dla swoich bliskich.
# Kiedy nadarzy się okazja, aby dać im prezent (święta, urodziny, rocznicę),
# program losowo wybierze jeden (i być może miejsca, w których możesz go zdobyć).

from random import choice

def main():
    gifts = [
        ('Róże', 'Kwiaciarnia'),
        ('Kolacja', 'Restauracja'),
        ('Skok ze spadochronem', 'Aeroklub'),
        ('Dzień w Spa', 'Spa'),
        ('Karty Pockemon', 'InMedio'),
        ('Karty Harry Potter', 'Empik'),
        ('Wspólne wędkowanie', 'Rzeka, Jezioro'),
        ('Koncert', 'E-bilet'),
        ('Impreza', 'Club'),
        ('Tydzień razem', 'Działka')
    ]
    gifts = dict(gifts)
    print(f'na prezent proponuję {choice(list(gifts.keys))}, a kupisz to w ')


main()
