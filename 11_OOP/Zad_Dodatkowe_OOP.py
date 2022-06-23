class Stos():
    def __init__(self, lifo):
        self.lifo = lifo


    def wyświetl(self):
        print('Stos:', self.lifo)


    def sprawdź(self):
        return len(self.lifo) == 0

    def dodanie(self, item):
        self.lifo.append(item)


    def wyjęcie(self):
        return self.lifo.pop(-1)


def main():
    s = Stos([3, 2, 7, 9, 'txt'])
    s.wyświetl()
    print(s.sprawdź())
    s.dodanie('Adam')
    s.wyświetl()
    print(s.lifo)
    print(s.wyjęcie())
    s.wyświetl()


if __name__ == "__main__":
    main()