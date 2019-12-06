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

# name = input('What is your name? ')
# skill = input('What is your skill? ')
# little = Student_monsters(name, skill, '001', 'B')
# # print(little.get_name())
# print(little.student_grade())
# print(little.get_uni_id())