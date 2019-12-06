# Define Monsters class

class Monsters():
    def __init__(self, name):
        self.__name = name
        self.skills = []

    def enrol(self, name):
        return 'New student: ' + name

    def get_name(self):
        return self.__name

    def add_skills(self, skills):
        self.skills.append(skills)



# name = input('What is your name? ')
# skill = input('What is your skill? ')
# little = Monsters(name, skill)
# # print(little.get_name())
# print(little.enrol(name))