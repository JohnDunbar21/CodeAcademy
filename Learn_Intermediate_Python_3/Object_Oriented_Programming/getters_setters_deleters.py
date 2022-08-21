class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # getter
  def get_name(self):
    return self._name

  # setter
  def set_name(self, new_name):
    self._name = new_name

  # deleter
  def del_name(self):
    del self._name
    print("Name attribute reset to: None")

e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
e2.set_name("Martha")
print(e2.get_name())