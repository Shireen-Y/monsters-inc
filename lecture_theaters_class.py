from building_class import *

class Lecture_theaters(Building):
    def __init__(self, location, hall_number):
        super().__init__(location)
        self.hall_number = hall_number

