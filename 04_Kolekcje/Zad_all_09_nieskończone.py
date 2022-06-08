# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi,
# drukowanymi lub zaczynając od dużej litery).
s_subject = []
for user in range(1, 6):
    s_subject.append(input(f'Użytkowniku {user}, podaj 4 przedmioty szkolne jakie lubiłeś, oddziel je spacjami ->'))
print(s_subject)
