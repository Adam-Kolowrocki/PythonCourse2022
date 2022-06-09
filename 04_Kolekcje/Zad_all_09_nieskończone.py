# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
# drukowanymi lub zaczynając od dużej litery).
s_subject_list = []
for user in range(1, 6):
    s_subject_list.append(input(f'Użytkowniku {user}, podaj 4 przedmioty szkolne jakie lubiłeś, oddziel je spacjami ->'))
print(s_subject_list)
for subject in s_subject_list:
    subject.lower()
print(s_subject_list)



"""for name in list_of_all:
    if list_of_all.count(name) >= 3:
        popular_names.append(name)
popular_names_set = set(popular_names)
print(popular_names_set)"""