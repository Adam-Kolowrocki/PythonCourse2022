# Utwórz dowolną krotkę zawierającą kilka wartości np. 10.
# Pozwól użytkownikowi podać dowolny index oraz wartość.
# Spróbuj w krotce podmienić wartość na zadanym indeksie. Obsłuż błąd

start_tuple = (4, 6, 9, 10, 2, 5, 12, 15, 16, 19, 26)
def get_user_data():
    user_ind = input(f'Podaj index wartości do zmiany, z zakresu od 0 do {len(start_tuple) - 1} -> ')
    user_val = input(f'Podaj nową wartość elementu o indeksie {user_ind} -> ')
    return user_ind, user_val


def replace():
    user_ind, user_val = get_user_data()
    try:
        start_tuple[user_ind] = start_tuple(user_val)
        print(f'Wartość {start_tuple[user_ind]} została zmieniona na {user_val}.')
    except TypeError:
            print(f'Nie można modyfikować krotki')
    return


def main():
    replace()

if __name__ == "__main__":
    main()
