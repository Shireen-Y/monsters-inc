from spooky_workshops_class import *
from student_monsters_class import *

student_monster1 = Student_monsters('Jimmy', '1', 'A')
student_monster2 = Student_monsters('James', '2', 'B')
student_monster3 = Student_monsters('Jimbob', '3', 'C')
students_list = []
students_list.extend([student_monster1, student_monster2, student_monster3])

spooky_workshop1 = Spooky_workshops('Scarinometry', 'Mrs Elen', 'Building A')
spooky_workshop2 = Spooky_workshops('Science of Scaring', 'Mr Blake', 'Building B')
spooky_workshop3 = Spooky_workshops('Fighting', 'Mrs Schmoney', 'Building C')
running_workshop = []
running_workshop.extend([spooky_workshop1, spooky_workshop2, spooky_workshop3])


while True:
    print('1- Create Monster')
    print('2- List of all workshops')
    print('3- Add student to spooky workshop')
    print('4- See student grade')
    print('5- Print full information of student')
    print('6- Search for student by name')
    user_input = input('Choose one of the above options or enter exit: ')
    if user_input == '1':
        print('You have chosen option 1 - Create Monster')
        name = input('What is the students name? ')
        id = input('What is the students university ID? ')
        grade = input('What is the students grade? ')
        print('Thank you, please wait a moment..')
        new_student = Student_monsters(name.capitalize(), id, grade)
        students_list.extend([new_student])
        print(new_student.get_name() + ' has been added successfully, thank you!')

    elif user_input == '2':
        print('You have chosen option 2 - List of all workshops')
        for subject in running_workshop:
            print(subject.scary_subject)

    elif user_input == '3':
        print('You have chosen option 3 - Add student to spooky workshop')
        workshop = input('Select a workshop to add the student to: ')
        stu = input('Please enter the ID of the student you wish to add to this workshop: ')
        for student in students_list:
            if stu == student.get_uni_id():
                #student_chosen = student
                for subject in running_workshop:
                    if workshop == subject.scary_subject:
                        #workshop_chosen = subject
                        subject.add_student(student)
                        print(f'The following students with ID: {subject.list_student_id()}, has been added')

    elif user_input == '4':
        print('You have chosen option 4 - See student grade')
        student_id = input('What is the student ID? ')
        for student in students_list:
            if student_id == student.get_uni_id():
                print('Student grade: ' + student.get_grade())

    elif user_input == '5':
        print('You have chosen option 5 - Print full information of student')
        student_id = input('What is the student ID? ')
        for student in students_list:
            if student_id == student.get_uni_id():
                print(f"Name: {student.get_name()}")
                print(f"Uni ID: {student.get_uni_id()}")
                print(f"Grade: {student.get_grade()}")

    elif user_input == '6':
        print('You have chosen option 6 - Search for student by name')
        stu_name = input('What is the students name? ')
        for student in students_list:
            if stu_name == student.get_name():
                print(f"Name: {student.get_name()}")
                print(f"Uni ID: {student.get_uni_id()}")
                print(f"Grade: {student.get_grade()}")

    elif user_input == 'exit':
        break


# Ask for info
# Evaluate info
# Say which option you chose
# Create monster
# List all workshops
# Add student to spooky workshop
# See students grade
# Print full info for students
# Search for student by name