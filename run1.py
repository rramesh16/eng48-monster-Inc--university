# This is the run file that takes in user's input, evaluates the input and displays the required info

from monster_class import *
from student_monster_class import *
from spooky_workshop_class import *
import time
print("Welcome to the Monster University admin system!")
while True:
    print('Please choose an option from below:')
    print("1: Enrol a student")
    print("2: List all the workshop")
    print("3: Add student to spooky workshop")
    print("4: See a student's grade")
    print("5: print a student's full information")
    print("6: search for a student by name")
    user_input = input("Please enter the option number...")
    if user_input == '1':
        print('You would like to enrol a student.')
        name = input("What is the student's name?")
        uni_id = input("Assign a student ID:")
        grade = input("Lastly, please input student's current grade:")
        studentList.append(Student_monster(name, uni_id, grade))
        print(f" Student: {name} is added to the system. Please choose another option or enter 'end' to exit.")

    elif user_input == '2':
        print('You would like to list all the workshops')
        for object in workshop_list:
            print(f' Scary_subject: {object.subject}, staff: {object.staff}, location: {object.location}')
        print("That's all the workshop. Please choose another option or enter 'end' to exit.")

    elif user_input == '3':
        print('You would like to add a student to the Spooky workshop')
        for object in workshop_list:
            print(f' Scary_subject: {object.subject}, staff: {object.staff}, location: {object.location}')
        subject = input('Please enter the name of the scary_subject from the list above:')
        for students in studentList:
            print(f'Name: {students.names}, Uni_ID: {students.uni_id}')
        # print the list of student
        # actually select a student object to add to list of student in workshop
        student = input('Enter the name or the id of the student:')
        for students in studentList:
            if students.uni_id == student:
                if subject == 'Make_Slime':
                    workshop1.add_student(student)
                    print(f'Updated list of students signed for workshop 1: {workshop1.students}')
                elif subject == 'Baking':
                    workshop2.add_student(student)
                    print(f'Updated list of students signed for workshop 2: {workshop2.students}')
                elif subject == 'Origami':
                    workshop3.add_student(student)
                    print(f'Updated list of students signed for workshop 3: {workshop3.students}')
            elif students.names == student:
                if subject == 'Make_Slime':
                    workshop1.add_student(student)
                    print(f'Updated list of students signed for workshop 1: {workshop1.students}')
                elif subject == 'Baking':
                    workshop2.add_student(student)
                    print(f'Updated list of students signed for workshop 2: {workshop2.students}')
                elif subject == 'Origami':
                    workshop3.add_student(student)
                    print(f'Updated list of students signed for workshop 3: {workshop3.students}')
        print(f" {student} is now added to the workshop {subject}. Please choose another option or enter 'end' to exit")

    elif user_input == '4':
        print("'You would like to view a student's grade")
        student_id = input("Please enter the student's uni id:")
        for student in studentList:
            if student.uni_id == student_id:
                print(f"Grade: {student.get_grade()}")
        print("Please choose another option or enter 'end' to exit")

    elif user_input == '5':
        print("You would like to print all the information of a student")
        student_id = input("Please enter the student uni id:")
        for student in studentList:
            if student.uni_id == student_id:
                print(f"Uni id: {student.uni_id}, name: {student.names}, grade: {student.get_grade()}")
        print("Please choose another option or enter 'end' to exit")

    elif user_input =='6':
        print("You would like to search for a student by name")
        student_name = input("Please enter the student's name: ")
        for student in studentList:
            if student.names == student_name:
                print(f"Uni id: {student.uni_id}, name: {student.names}, grade: {student.get_grade()}")
        print("Please choose another option or enter 'end' to exit")

    elif user_input == 'end':
        break
    else:
        print("Sorry I didn't get that. Please enter your option carefully.")
        time.sleep(1.5)
print("Have a good day!")








# ask for info
# evaluate infor
# say which option you chose

# Create a monster --1


# List all workshop --2


# Add student to spooky workshop --3


# See students grade --4


# print full information of student --5


# Search for student by name --6