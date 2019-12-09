# Running
from monsters_class import *
from student_monsters_class import *
from spooky_workshops_class import *


# student2 = Monsters('Bobby', ['Tall', 'Impeccable eyesight', 'Long limbs'])

name = input('What is your name? ')
student1 = Student_monsters(name, 1, 7)
student1.set_grade(7)
print('Monster name: ' + (name.capitalize()))
print(f'Uni_ID: {student1.get_uni_id()}')
print(f'Grade: {student1.get_grade()}')

new_workshop = Spooky_workshops('Scarin-o-metry', 'James', 'London')
new_workshop.add_student(student1)
print(name.capitalize() + ' will be added into: ' + new_workshop.name)

