# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystkie listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

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

print(dictionary['Polska'])
print(list(dictionary))
print(len(dictionary))