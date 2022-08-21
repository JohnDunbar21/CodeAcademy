class School:
    
    def __init__(self, name, level, numberOfStudents):
        self._name = name
        self._level = level
        self._numberOfStudents = numberOfStudents

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_number_of_students(self):
        return self._numberOfStudents

    def set_number_of_students(self, numberOfStudents):
        self._numberOfStudents = numberOfStudents

    def __repr__(self):
        return "A {} school named {} with {} students.".format(self._level, self._name, self._numberOfStudents)

class PrimarySchool(School):

    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self._pickupPolicy = pickupPolicy

    def get_pickup_policy(self):
        return self._pickupPolicy

    def __repr__(self):
        return super().__repr__()

class HighSchool(School):

    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self._sportsTeams = sportsTeams

    def get_sports_teams(self):
        return self._sportsTeams

    def __repr__(self):
        return "{} {} school has the following sports teams: {}.".format(self._name, self._level, self._sportsTeams)


school1 = School("Ursuline", "high", 9000)
print(school1.get_name())
print(school1.get_number_of_students())
print(school1.get_level())
school1.set_number_of_students(8000)
print(school1.get_number_of_students())
print(school1)
print("\n")
primary1 = PrimarySchool("St John of God", 2500, "Pickup after 15:30, grounds close at 17:00")
print(primary1.get_name())
print(primary1.get_number_of_students())
print(primary1.get_level())
print(primary1.get_pickup_policy())
print(primary1)
print("\n")
highschool1 = HighSchool("RGU College", 6000, "Rugby, Football, Cricket, Hockey, Table Tennis, and Track")
print(highschool1.get_name())
print(highschool1.get_number_of_students())
print(highschool1.get_level())
print(highschool1.get_sports_teams())
print(highschool1)