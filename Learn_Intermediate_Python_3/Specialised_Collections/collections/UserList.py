"""
The 'UserList' wrapper container lets us create our own list as well! This class contains all of 
the functionality of a regular 'list', but it also has a property called 'data' which allows us to 
access the list contents directly.
"""


from collections import UserList

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

class ListSorter(UserList):

  def append(self, value):
    self.data.append(value)
    self.data.sort()

sorted_list = ListSorter(data)
sorted_list.append(2)

print(sorted_list)