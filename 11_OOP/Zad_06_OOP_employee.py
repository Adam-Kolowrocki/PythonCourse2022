# Utwórz klasę Pracownik. Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staż pracy.
# Pracownik powinien miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia.
# Pracownik powinien odprowadzać podatek o wysokoci zależnej od swoich zarobków
# oraz minimalną składkę zdrowotną.
# Pracownik powinien mieć pole typu boolowskiego zawierające status studenta.
# Jeśli pracownik jest studentem, jego składka zdrowotna wynosi 0%.
# Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska
# wraz z nazwą firmy .com tworzą adres mailowy. Np.
# Adam Kowalski Love Python Company
# email -> smkwlsk@lovepythoncompany.com
class Employee:
    company = 'CooperMine'

    def __init__(self, name, surname, position, salary, seniority, student):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.seniority = seniority
        self.student = student

    def salary_inc(self, salary, seniority):
        new_salary = salary + ((salary * 0.1) * seniority)
        return new_salary

    def tax(self, salary):
        tax_rate = 0
        if salary < 4000:
            tax_rate = 0.1
        elif 4001 < salary < 9000:
            tax_rate = 0.13
        elif salary > 9001:
            tax_rate = 0.15
        return tax_rate

    def health_ins(self, salary):
        if not Employee(self.student):
            health_ins = salary * 0.03
        else:
            health_ins = 0
        return health_ins

    def email(self):
        return '{}.{}@company.com'.format(self.name, self.surname)


def main():
    kowalski = Employee('Jan', 'Kowalski', 'worker', 6800, 6, False)
    nowak = Employee('Marcin', 'Nowak', 'worker', 3800, 1, True)
    lisicki = Employee('Tomasz', 'Lisicki', 'worker', 4600, 3, True)
    malinowski = Employee('Janusz', 'Malinowski', 's.worker', 7900, 6, False)
    juszczak = Employee('Marian', 'Juszczak', 'manager', 9900, 8, False)
    print(kowalski.email())
    print(nowak.salary_inc())


if __name__ == '__main__':
    main()
