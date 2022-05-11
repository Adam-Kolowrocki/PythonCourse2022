
learning_hours = float(input('Ile godzin trwa kurs? '))
my_time = float(input('Ile godzin w tygodniu poświęcisz? '))
full_cours = learning_hours / my_time
resoult2 = round(full_cours, 1)

print('Zakładając, że poświęcisz', my_time, 'godzin w tygodniu na kurs który trwa', learning_hours, 'godzin, ukończysz go w:' , resoult2, 'tygodni')
