class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student('Pepe', (10, 20, 30, 40))
student2 = Student('Paco', (50, 60, 70, 80))
print(student.name)
print(student.grades)

# Two ways to call the method:
print(Student.average_grade(student))
print(student.average_grade())

print(student2.name)
print(student2.average_grade())