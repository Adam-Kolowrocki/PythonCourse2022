# Stwórz własną implementację kolejki FIFO.
# Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyświetlenie kolejki, sprawdzenie, czy jest pusta,
# dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).
# Utwórz kilka obiektów klasy Queue z różnymi parametrami.

class Queue:
    def __init__(self, fifo):
        self.fifo = fifo

    def wyświetl(self):
        print('Queue:', self.fifo)

    def sprawdź(self):
        return len(self.fifo) == 0

    def dodanie(self, item):
        self.fifo.append(item)

    def wyjęcie(self):
        return self.fifo.pop(0)


def main():
    q = Queue([3, 2, 7, 9, 'txt'])
    q.wyświetl()
    print(q.sprawdź())
    q.dodanie('Adam')
    q.wyświetl()
    print(q.fifo)
    print(q.wyjęcie())
    q.wyświetl()


if __name__ == "__main__":
    main()
