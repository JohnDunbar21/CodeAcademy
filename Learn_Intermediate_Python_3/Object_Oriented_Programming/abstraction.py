from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
    new_id = 1
    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass

class Employee(AbstractEmployee):
    def say_id(self):
        print("My ID is {}.".format(self.id))

e1 = Employee()
e1.say_id()