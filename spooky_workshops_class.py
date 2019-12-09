# Define spooky workshops class

class Spooky_workshops():
    def __init__(self, scary_subject, staff, location):
        self.name = scary_subject
        self.staff = staff
        self.location = location
        self.students = []

    def add_student(self, student):
        self.students.append(student)


all_subjects = ['Scarin-o-metry', 'Science of Scaring', 'Fighting', 'Gym']

# Jim = Spooky_workshops('name', 'skills', 'id', 'grade', 'staff', 'location', all_subjects)
# print(Jim.list_of_all_subjects(all_subjects))
# print(Spooky_workshops.name)