from monsters_class import *

class Student_monsters():
    def __init__(self, name, skills, uni_id, grade):
        super().__init__(name, skills)
        self.uni_id = uni_id
        self.grade = grade

