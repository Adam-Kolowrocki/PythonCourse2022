# Stwórz własną implementację stosu LIFO.
# Klasa stos (Stack).
# Wśród metod powinny się znaleźć takie jak: wyświetlenie stosu,
# dodanie elementu do stosu (push), wyjęcie elementu ze stosu (pop).
# Utwórz kilka obiektów klasy Stack z różnymi parametrami.

class Stos:
    def __init__(self, lifo):
        self.lifo = lifo

    def wyświetl(self):
        print('Stos:', self.lifo)

    def dodanie(self, item):
        self.lifo.append(item)

    def wyjęcie(self):
        return self.lifo.pop(-1)


def main():
    s = Stos([3, 2, 7, 9, 'txt'])
    s.wyświetl()
    s.dodanie('Adam')
    s.wyświetl()
    print(s.wyjęcie())
    s.wyświetl()


if __name__ == "__main__":
    main()
