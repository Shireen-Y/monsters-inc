# Running
from monsters_class import *
from student_monsters_class import *
from spooky_workshops_class import *


# student2 = Monsters('Bobby', ['Tall', 'Impeccable eyesight', 'Long limbs'])

# name = input('What is your name? ')
# student1 = Student_monsters(name, 1, 7)
# student1.set_grade(7)
# print('Monster name: ' + (name.capitalize()))
# print(f'Uni_ID: {student1.get_uni_id()}')
# print(f'Grade: {student1.get_grade()}')
#
new_workshop = Spooky_workshops('maths', 'James', 'London')
#
# print(name.capitalize() + ' will be added into: ' + new_workshop.scary_subject)


student_monster1 = Student_monsters('Jimmy', '1', 'A')
student_monster2 = Student_monsters('James', '2', 'B')
student_monster3 = Student_monsters('Jimbob', '3', 'C')
new_workshop.add_student(student_monster3)
print(new_workshop.list_student_id())


students_list = []
students_list.extend([student_monster1, student_monster2, student_monster3])

spooky_workshop1 = Spooky_workshops('Scarin-o-metry', 'Mrs Elen', 'Building A')
spooky_workshop2 = Spooky_workshops('Science of Scaring', 'Mr Blake', 'Building B')
spooky_workshop3 = Spooky_workshops('Fighting', 'Mrs Schmoney', 'Building C')
runnning_workshop = []
runnning_workshop.extend([spooky_workshop1, spooky_workshop2, spooky_workshop3])
