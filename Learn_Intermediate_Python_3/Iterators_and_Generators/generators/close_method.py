"""
The generator method 'close()' is used to terminate a generator early.
Once the 'close()' method is called the generator is finished just like the end of a 'for loop'.
Any further iteration attempts will raise a 'StopIteration' exception.

The 'close()' method works by raising a 'GeneratorExit' exception inside the generator function.
The exception is generally ignored but can be handled using 'try' and 'except'.

Putting the 'yield' expression in a 'try' block we can handle the 'GeneratorExit' exception.
In this case, we simply print out a message.
Because we interrupted the automatic behavior of the 'close()' method, we must also use a 'break' to exit the loop or else a 'RuntimeError' will occur.
"""


def student_counter():
  for i in range(1,5001):
    try:
      yield i
    except:
      print("{Generator terminated}")
      break

student_generator = student_counter()
for student_id in student_generator:
  print(student_id)
  if student_id >= 100:
    student_generator.close()