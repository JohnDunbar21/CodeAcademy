"""
Since strings are also considered containers, the collections module also provides a container wrapper for the string class. 
This contains all of the functionality of a regular string, but it includes the string's data inside of a property called data. 
Inheriting from this class allows us to create our own version of a string!
"""


from collections import UserString

str_name = 'python powered patterned products'
str_word = 'patterned '

class SubtractString(UserString):

  def __sub__(self, item):
    if item in self.data:
      self.data = self.data.replace(item, '') 

subtract_string = SubtractString(str_name)
subtract_string - str_word