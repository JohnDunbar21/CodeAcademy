"""
The 'contextlib' module allows for the creation of a context manager with the use of a 
generator function (a function that uses 'yield' instead of 'return') and the contextlib 
decorator - '@contextmanager'. Instead of creating a class and definining '__enter__' and 
'__exit__' methods, we can use a simple function.
"""


from contextlib import contextmanager

@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()


with poem_files('poem.txt', 'a') as opened_file:
  print('Inside yield')
  opened_file.write('Rose is beautiful, Just like you.')