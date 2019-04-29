class Student:

    def __init__(self, name, cpr):
        self.__name = name
        self.__cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return f'I´m Anna {self.name}´s daughter i was created by to students'

    def __repr__(self):
        return f'{self.name}, {self.cpr}'

    def __str__(self):
        return f'name: {self.name} \ncpr: {self.cpr}'
        

