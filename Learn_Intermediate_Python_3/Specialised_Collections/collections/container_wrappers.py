"""
In Python, wrappers are modifications to functions or classes which change the behavior in some way. 
They are called wrappers because they “wrap” around the existing code to modify it. 
This is most commonly used with function wrapping, but we can also wrap classes.

In the case of containers, the collections class has three different wrapper classes set up for us to modify:

- UserDict

- UserList

- UserString
"""


class Customer:
 
  def __init__(self, name, age, address, phone_number):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number


class CustomerWrap(Customer):
 
  def __init__(self, name, age, address, phone_number):
    self.customer = Customer(name, age, address, phone_number)
 
  def display_customer_info(self):
    print('Name: ' + self.customer.name)
    print('Age: ' + str(self.customer.age))
    print('Address: ' + self.customer.address)
    print('Phone Number: ' + self.customer.phone_number)


customer = CustomerWrap('Dmitri Buyer', 38, '123 Python Avenue', '5557098603')
customer.display_customer_info()