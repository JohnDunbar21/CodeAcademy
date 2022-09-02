"""
'yield' differs from 'return' in two key ways:

1. Any code written after a 'yield' expression will execute on the next iteration of the iterator, where
code written after a 'return' statement will not execute.

2. The 'yield' expression will suspend the execution of the function and preserve any local variables that
exist within the function. The 'return' statement will terminate the function immediately and return the result(s)
to the caller.

Like all objects, the iterator object returned by a generator function can be stored in a variable to be used later,
and be iterated through as needed.
"""

def class_standing_generator():
  yield 'Freshman'
  yield 'Sophomore'
  yield 'Junior'
  yield 'Senior'

class_standings = class_standing_generator()

for class_level in class_standings:
  print(class_level)