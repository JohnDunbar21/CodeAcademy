"""
To pipeline generators, the output of one generator function can be the input of another generator function.
That resulting generator can then be used as input for another generator function, and so on.

Pipeline generators are also often referred to as nested generators.
"""

def course_generator():
    yield ("Computer Science", 5)
    yield ("Art", 10)
    yield ("Business", 15)

def add_five_students(courses):
  for course,num_students in courses:
    yield (course, num_students + 5)

increased_courses = add_five_students(course_generator())

for course in increased_courses:
  print(course)