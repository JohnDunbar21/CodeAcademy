"""
One of the two approaches of creating context managers is referred to as the class-based approach. 
The class-based approach of writing context managers requires explicitly defining and implementing 
the following two methods inside of a class:

- An '__enter__' method:

        The '__enter__' method allows for the setup of context managers. 
        This method commonly takes care of opening resources (like files). 
        This method also begins what is known as the runtime context - the 
        period of time in which a script runs. In our previous examples, it 
        was the time in which the code passed into the 'with' statement code 
        block was executed (basically everything under the 'with' statement).

- An '__exit__' method:

        The '__exit__' ensures the breakdown of the context manager. This method 
        commonly takes care of closing open resources that are no longer in use.
"""


class PoemFiles:
  
  def __init__(self):
    print('Creating Poems!')

  def __enter__(self):
    print('Opening poem file')

  def __exit__(self, *exc):
    print('Closing poem file')

with PoemFiles() as manager:
  print('Hope is the thing with feathers') # executes after __enter__ but before __exit__