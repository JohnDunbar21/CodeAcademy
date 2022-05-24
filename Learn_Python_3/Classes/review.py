class Student:
    def __init__ (self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {"2/3/2019": True}

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self, grades):
        average = 0
        for item in self.grades:
            average += item
        final_avg = average / len(self.grades)
        return final_avg


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self, score):
        if self.score >= self.minimum_passing:
            return "You are currently passing!"

    

pieter.add_grade(Grade(100))