"""
The generator method 'throw()' provides the ability to throw an exception inside the generator from the caller point.
This can be useful if we need to end the generator once it reaches a certain value or meets a particular condition.
"""


def student_counter():
  for i in range(1,5001):
    yield i

student_generator = student_counter()
for student_id in student_generator:
  if student_id > 100:
    student_generator.throw(ValueError, "Invalid student  ID")
  
  print(student_id)