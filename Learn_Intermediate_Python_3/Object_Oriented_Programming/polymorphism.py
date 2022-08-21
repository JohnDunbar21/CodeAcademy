class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is "+str(self.id))

class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("I am an Admin") # overrides the parent class method. 

class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am in charge.")

meeting = [Employee(), Admin(), Manager()]
for item in meeting:
    item.say_id()