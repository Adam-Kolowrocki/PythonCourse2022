class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, student_avg, scholarship):
        self.name = name
        self.last = last
        self.student_avg = student_avg
        self.scholarship = scholarship

    @property
    def fullname(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @property
    def email(self):
        return f'{self.name.lower()}.{self.last.lower()}@university.com'

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            self.scholarship = True
        else:
            self.scholarship = False


obj_anna = Student('anna', 'kowalska', 4.6, None)
obj_arek = Student('arkadiusz', 'nowak', 3.8, None)


print(obj_anna.email)
obj_anna.grant_scholarship()
# print(Student.email(obj_anna))
