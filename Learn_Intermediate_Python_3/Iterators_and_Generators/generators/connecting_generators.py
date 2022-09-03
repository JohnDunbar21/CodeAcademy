"""
Connecting generators is similar to using the itertools 'chain()' function to combine iterators into a single iterator.
In order to connect generators, we use the 'yield from' statement.

"""


def science_students(x):
  for i in range(1,x+1):
    yield i

def non_science_students(x,y):
  for i in range(x,y+1):
    yield i
  
def combined_students():
  yield from science_students(5)
  yield from non_science_students(10,15)
  yield from non_science_students(25,30)

student_generator = combined_students()
for student in student_generator:
  print(student)