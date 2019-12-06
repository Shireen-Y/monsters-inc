# Running
from monsters_class import *
from student_monsters_class import *
from spooky_workshops_class import *
from building_class import *
from lecture_theaters_class import *

student2 = Monsters('Bobby', ['Tall', 'Impeccable eyesight', 'Long limbs'])

# What is your name? input('What is your name?')
# Assign input to 'get_name'
# Print name

name = input('What is your name? ')
skill = input('What is your skill? ')
little = Monsters(name, skill)
# print(little.get_name())
print(little.enrol(name))
get_id = Student_monsters(name, skill, '001', 'B')

all_subjects = ['Scarin-o-metry', 'Science of Scaring', 'Fighting', 'Gym']

student1 = Spooky_workshops(name, skill, get_id.get_uni_id(), get_id.student_grade('B'),
                            'staff', 'location', all_subjects)
print('These are the workshops that we are currently offering: ')
print(student1.list_of_all_subjects(all_subjects))