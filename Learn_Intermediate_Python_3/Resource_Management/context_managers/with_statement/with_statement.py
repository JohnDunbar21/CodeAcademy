"""
The 'with' statement is the most common and pythonic way of invoking context managers in python.

The alternative to using 'with' would require us to manually open (using 'open()') and close (using 'close()') 
the file we are working on. By using the 'with' statement, it serves as a context 
manager where files are automatically closed after script completion and we don't ever have to worry about 
the possibility of forgetting to close a resource. Remember, leaving our resources open will hog up our 
finite computer resources. We are never guaranteed that Python will close the file for us if we happen 
to forget to do it.
"""

# no context management
try:
  open_file = open('Learn_Intermediate_Python_3\Resource_Management\context_managers\with_statement\doc.txt', 'r')
  print(open_file.read())
finally:
  open_file.close()

# context management
with open('Learn_Intermediate_Python_3\Resource_Management\context_managers\with_statement\doc.txt', 'r') as open_file:
  print(open_file.read())