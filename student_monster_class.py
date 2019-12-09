# student monster class file
from monster_class import *


class Student_monster(Monster):
    def __init__(self, name,  uni_id, grade):
        super().__init__(name)
        self.uni_id = uni_id
        self.__grade = grade


# Grade getter
    def get_grade(self):
        return self.__grade

# Grade setter
    def set_grade(self, grade):
        self.__grade = grade




# Creating students

student1 = Student_monster('Sulley', '001', 'A')
student1.set_grade('A')
# print(student1.get_grade())

student2 = Student_monster('Mike', '002', 'A')
student2.set_grade('B')
# print(student2.get_grade())

student3 = Student_monster('Roz', '003', 'C')
student3.set_grade('C')
# print(student3.get_grade())

student4 = Student_monster('Randall', '004', 'D')
student4.set_grade('C')
# print(student4.get_grade())

student5 = Student_monster('Fungus', '005', 'C')
student5.set_grade('D')
# print(student5.get_grade())

studentList =[]
studentList.append(Student_monster('Sulley', '001', 'A'))
studentList.append(Student_monster('Mike', '002', 'A'))
studentList.append(Student_monster('Roz', '003', 'C'))
studentList.append(Student_monster('Randall', '004', 'D'))
studentList.append(Student_monster('Fungus', '005', 'C'))

# Iterate over the student list and print
# for students in studentList:
#     print(f'Name: {students.names}, Uni_ID: {students.uni_id}')

