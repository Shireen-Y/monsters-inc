from monsters_class import *

class Student_monsters(Monsters):
    def __init__(self, name, uni_id, grade):
        super().__init__(name)
        self.__uni_id = int(uni_id)
        self.__grade = grade

    def student_grade(self, name, grade):
        return name + ' this is your grade: ' + self.__grade

    def get_uni_id(self):
        return self.__uni_id

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


