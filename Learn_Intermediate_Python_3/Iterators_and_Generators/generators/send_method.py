"""
The 'send()' method allows us to send a value to a generator using the 'yield' expression.
If you assign 'yield' to a variable the argument passed to the 'send()' method will be assigned to that variable.
Calling 'send()' will also cause the generator to perform an iteration.

The 'send()' method can control the value of the generator when a second variable is introduced.
One variable holds the iteration value and the other holds the value passed through 'yield'.
"""


MAX_STUDENTS = 50

def get_student_ids():
  student_id = 1
  while student_id <= MAX_STUDENTS:
    n = yield student_id
    if n is not None:
      student_id = n
      continue
    student_id += 1

student_id_generator = get_student_ids()
for i in student_id_generator:
  if i == 1:
    i = student_id_generator.send(25)

  print(i)