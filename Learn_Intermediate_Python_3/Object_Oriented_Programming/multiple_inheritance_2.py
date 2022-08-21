class Employee:
    new_id = 1

    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1

    def say_id(self):
        print("My id is "+str(self.id))

class User:
    def __init__(self, username, role="customer"):
        self.username = username
        self.role = role
    
    def say_user_info(self):
        print("My username is {}".format(self.username))
        print("My role is {}".format(self.role))

class Admin(Employee, User):
    def __init__(self):
        super().__init__()
        User.__init__(self, self.id, "Admin")
    
    def say_id(self):
        super().say_id()
        print("I am an Admin") # overrides the parent class method. 

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()