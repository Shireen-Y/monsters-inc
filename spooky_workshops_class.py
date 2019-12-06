# Define spooky workshops class
from student_monsters_class import *
from monsters_class import *

class Spooky_workshops(Student_monsters, Monsters):
    def __init__(self, name, skills, uni_id, grade, staff, location, list_student_monsters = [],
        scary_subject = []):
        super().__init__(name, skills, uni_id, grade)
        self.scary_subject = scary_subject
        self.staff = staff
        self.list_student_monsters = list_student_monsters
        self.location = location

class Spooky_workshops():
    def __init__(self, scary_subject, staff, location):
        self.name = scary_subject
        self.staff = staff
        self.location = location
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# all_subjects = ['Scarin-o-metry', 'Science of Scring', 'Fighting', 'Gym']
#
# Jim = Spooky_workshops('name', 'skills', 'id', 'grade', 'staff', 'location', all_subjects)
# print(Jim.list_of_all_subjects(all_subjects))