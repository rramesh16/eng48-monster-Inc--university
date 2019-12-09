# Spooky workshop class
from student_monster_class import *
from monster_class import *
from building_class import *

class Spooky_workshop(Building):
    def __init__(self, scary_subject, staff, location):
        super(). __init__(location)
        self.subject = scary_subject
        self.staff = staff
        self.list_student_monsters = studentList
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Adding workshop1
workshop1 = Spooky_workshop('Make_Slime', 'Mr.Ronald', 'East Wing')
workshop1.add_student('Sulley')
workshop1.add_student('Mike')
workshop1.add_student('Fungus')

#Adding workshop2
workshop2 = Spooky_workshop('Baking', 'Mrs.Gren', 'South Wing')
workshop2.add_student('Randall')
workshop2.add_student('Mike')
workshop2.add_student('Roz')

#Adding workshop3
workshop3 = Spooky_workshop('Origami', 'Ms. Natasha', 'Library')
workshop3.add_student('Sulley')
workshop3.add_student('Fungus')
workshop3.add_student('Roz')

workshop_list = []
workshop_list.append(workshop1)
workshop_list.append(workshop2)
workshop_list.append(workshop3)

# Iterate over the list of workshops and print
# for object in workshop_list:
#     print(f' Scary_subject: {object.subject}, staff: {object.staff}, location: {object.location}')









# print(example_monster.skills)
# spooky_workshop_list =[]
# spooky_workshop_list.append(Spooky_workshop('Slime_making', '001', 'A'))
# spooky_workshop_list.append(Spooky_workshop('Mike', '002', 'A'))
# spooky_workshop_list.append(Spooky_workshop('Roz', '003', 'C'))
# spooky_workshop_list.append(Spooky_workshop('Randall', '004', 'D'))
# spooky_workshop_list.append(Spooky_workshop('Fungus', '005', 'C'))