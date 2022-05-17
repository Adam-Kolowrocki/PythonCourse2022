sum_grades = 0
for i in range(3):
    subject = input('Podaj nazwę przedmiotu: ')
    grade = int(input(f'Podaj ocenę z {subject}: '))
    print(f'Ocena z {subject} to {grade}')
    sum_grades += grade

print(f'Twoja średnia ocen z 3 przedmiotów to {round(sum_grades/3, 2)}')



#pierwszy = input('Podaj pierwszy przedmiot: ')
#drugi = input('Podaj drugi przedmiot: ')
#trzeci = input('Podaj trzeci przedmiot: ')
#grade_1 = input("Podaj 1 ocenę: ")
#grade_2 = input('podaj 2 ocenę: ')
#grade_3 = input('Podaj 3 ocenę: ')


#print(pierwszy + ":" + grade_1)
#print(drugi + ":" + grade_2)
#print(trzeci + ":" + grade_3)
#subject -> "Przedmiot szkolny: "
#grade -> "Ocena w skali 1-6: "
#wyświetl -> subject + ": " + grade