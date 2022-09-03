"""
'deque' containers are similar to lists, but they are optimized for appending and popping to the front and back, 
rather than having optimized accessing. Because of this, they are great for working with data where you don't need 
to access elements in the middle very often or at all.
"""


from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

supplies_deque = deque()
for line in csv_data:
  if line[2] == 'important':
    supplies_deque.appendleft(tuple(line))
  else:
    supplies_deque.append(tuple(line))

ordered_important_supplies = deque()
for i in range(0,25):
  ordered_important_supplies.append(supplies_deque.popleft())

ordered_unimportant_supplies = deque()
for j in range(0,10):
  ordered_unimportant_supplies.append(supplies_deque.pop())

"""
Any method containing 'left' such as 'appendleft()' or 'popleft()' applies to the front of a list.
"""