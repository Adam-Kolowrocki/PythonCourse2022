# Utwórz słownik dla 10 krajów Europy zawierający listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystkie listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły co najmniej w 3 krajach.

dictionary = {'Polska': ['Susanna', 'Julia', 'Sophia', 'Hannah', 'May', 'Lena', 'Alice', 'Olive', 'Laura', 'Maria'],
                 'Francja': ['Amelia', 'Anna', 'Bianka', 'Brigitte', 'Celina', 'Clara', 'Nikola', 'Eve', 'Francoise',
                             'Isabella'],
                 'Niemcy': ['Emilia', 'Mia', 'Hanna', 'Emma', 'Sofia', 'Mila', 'Lina', 'Ella', 'Leni', 'Clara'],
                 'Czechy': ['Anna', 'Adela', 'Barbra', 'Eliska', 'Carolina', 'Katerine', 'Cristine', 'Maria',
                            'Natallie', 'Nikola'],
                 'Szwecja': ['Alice', 'Maja', 'Vera', 'Alma', 'Selma', 'Elsa', 'Lilly', 'Ella', 'Astrid', 'Wilma'],
                 'Włochy': ['Sofia', 'Giulia', 'Alice', 'Ginevra', 'Emma', 'Giorgia', 'Greta', 'Martina', 'Beatrice'],
                 'Hiszpania': ['Alice', 'Esmeralda', 'Jimena', 'Lola', 'Lucia', 'Maria', 'Savannah', 'Sofia'],
                 'Wielka_Brytania': ['Olivia', 'Amelia', 'Isla', 'Ava', 'Mia', 'Ivy', 'Lily', 'Isabella', 'Rosie',
                                     'Sophia'],
                 }

list_of_all = list(dictionary['Polska']) + list(dictionary['Francja']) + list(dictionary['Niemcy']) + \
              list(dictionary['Czechy']) + list(dictionary['Szwecja']) + list(dictionary['Włochy']) + \
              list(dictionary['Hiszpania']) + list(dictionary['Wielka_Brytania'])
popular_names = []
for name in list_of_all:
    if list_of_all.count(name) >= 3:
        popular_names.append(name)
popular_names_set = set(popular_names)
print(popular_names_set)
