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
    proposed_gift = choice(list(gifts.items()))
    print(f'Na prezent proponuję {proposed_gift[0]}, a kupisz to w {proposed_gift[1]}')


if __name__ == "__main__":
    main()
