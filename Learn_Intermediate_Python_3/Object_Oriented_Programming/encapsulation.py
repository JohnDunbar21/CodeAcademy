class Employee():
    def __init__(self):
        self.id = None
        self._id = 4
        self.__id = 16
        

e = Employee()
print(dir(e))