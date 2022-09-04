"""
The '__exit__' method has three required arguments (in addition to 'self'):

- An exception type: which indicates the class of exception (i.e. 'AttributeError' class, or 'NameError' class)

- An exception value: the actual value of the error

- A traceback: a report detailing the sequence of steps that caused the error and all the details needed to fix the error.
"""


class PoemFiles:

  def __init__(self, poem_file, mode):
    print(' \n -- Starting up a poem context manager -- \n ')
    self.file = poem_file
    self.mode = mode

  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()

# this will throw an error in the __exit__ method
# with PoemFiles('poem.txt', 'r') as file:
#   print("---- Exception data below ----")
#   print(file.uppercasewords())

# Second
with PoemFiles('poem.txt', 'r') as file2:
   print(file2.read())
   print("---- Exception data below ----")