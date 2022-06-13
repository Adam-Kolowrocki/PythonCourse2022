# Stwórz listę 10 elementową (różne typy!).
# Pozwól użytkownikowi podać dowolny index. Podziel 1 przez liczbę pod indexem
# wybranym przez użytkownika. Obsłuż błędy.
def main():
    items = [12233, 123.133, 'text', 101001110, 0b10, 5j, True, False, {}, (2, 5), [5, 8], 9233.44, 6j, 'xd', None]

    try:
        id = int(input(f'Podaj wartość od 0 do 14 ->'))
        print(1 / items[id])
    except ValueError:
        print('Value Error')
    except TypeError:
        print('Type Error')
    except ZeroDivisionError:
        print('Can\'t divide by 0')
    except IndexError:
        print(f'Z duża wartość. 0 - {len(items) - 1}')


if __name__ == "__main__":
    main()
