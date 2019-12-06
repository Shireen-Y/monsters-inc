# Define Monsters class

class Monsters():
    def __init__(self, name):
        self.__name = name
        self.skills = []

    def get_name(self):
        return self.__name

    def add_skills(self, skills):
        self.skills.append(skills)
