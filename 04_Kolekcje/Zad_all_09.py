# 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty
# powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot. (Uwzględnij fakt, że użytkownicy mogą zapisać
# przedmioty małymi, drukowanymi lub zaczynając od dużej litery).
s_subjects = []
for user in range(1, 6):
    user_list = []
    for sub in range(1, 5):
        subject = input(f'Użytkowniku {user}, podaj przedmiot jaki lubiłeś w szkole ->')
        user_list.append(subject)
    s_subjects += user_list
s_subjects = str(s_subjects)
s_subjects = s_subjects.replace('[', '')
s_subjects = s_subjects.replace(']', '')
s_subjects = s_subjects.replace(',', '')
s_subjects_lower = s_subjects.lower()
s_subjects_list = s_subjects_lower.split()
subject_counter = {}

for subject in s_subjects_list:
    if subject in subject_counter:
        subject_counter[subject] += 1
    else:
        subject_counter[subject] = 1

v = list(subject_counter.values())
k = list(subject_counter.keys())
print(f'Najpopularniejszy przedmiot to {k[v.index(max(v))]}')
