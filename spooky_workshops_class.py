# Define spooky workshops class

class Spooky_workshops():
    def __init__(self, scary_subject, staff, location):
        self.scary_subject = scary_subject
        self.staff = staff
        self.location = location
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def list_student_id(self):
        stu_id = []
        for student in self.students:
            stu_id.extend([student.get_uni_id()])
        return stu_id



#all_subjects = ['Scarin-o-metry', 'Science of Scaring', 'Fighting', 'Gym']

# Jim = Spooky_workshops('name', 'skills', 'id', 'grade', 'staff', 'location', all_subjects)
# print(Jim.list_of_all_subjects(all_subjects))
# print(Spooky_workshops.name)