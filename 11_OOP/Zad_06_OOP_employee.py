# Utwórz klasę Pracownik.
# Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staż pracy.
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
    def __init__(self, name, surname, position, salary, seniority):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.seniority = seniority
