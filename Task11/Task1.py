class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
    def __str__(self):
        return print(f"Name: {self.fname} {self.lname}, Years old {self.age}, gender: {self.gender}")
class Student(Person):
    def __init__(self, fname, lname, age, gender, grade, succses):
        self.grade = grade
        self.succses = succses
        Person.__init__(self, fname, lname, age, gender)
    def __str__(self):
        Person.__str__(self)
        print(f"Grade: {self.grade}, Succses: {self.succses}")

    def kicked_out(self):
        del self

class Teacher(Person):
    def __init__(self, fname, lname, age, gender, experience_work, *teacher_for_class):
        self.teacher_for_class = teacher_for_class
        self.experience_work = experience_work
        Person.__init__(self, fname, lname, age, gender)
    def __str__(self):
        Person.__str__(self)
        print(f"Teacher for classes: {self.teacher_for_class}, Work experience: {self.experience_work}")
    def dismissal(self):
        del self

stud1 = Student("Danil", "Roscha", 20, "Male", "3 course", "A+")
stud1.__str__()

teach1 = Teacher("Milena", "McCallen", 29, "Female", 9, "7B", "9A", "11G")
teach1.__str__()

teach12 = Teacher("Ilena", "McCallen", 29, "Female", 9, "7B", "9A", "11G")
teach12.__str__()
teach12.dismissal()
teach12.__str__()
