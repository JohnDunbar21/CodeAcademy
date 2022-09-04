"""
The OrderedDict container allows us to access values using keys, but it also preserves the order of the elements inside of it.

When using an 'OrderedDict', we are able to use its methods for moving the data around. 
We can move an element to the back or front and pop the data from the back or front of the 'OrderedDict'.

Note: These two methods also accept boolean arguments which determine if the element is moved / popped from the front or back of the 'OrderedDict'.
"""


from collections import OrderedDict

# The first 15 orders are provided
order_data = [['Order: 1', 'purchased'],
              ['Order: 2', 'purchased'],
              ['Order: 3', 'purchased'],
              ['Order: 4', 'returned'],
              ['Order: 5', 'purchased'],
              ['Order: 6', 'canceled'],
              ['Order: 7', 'returned'],
              ['Order: 8', 'purchased'],
              ['Order: 9', 'returned'],
              ['Order: 10', 'canceled'],
              ['Order: 11', 'purchased'],
              ['Order: 12', 'returned'],
              ['Order: 13', 'purchased'],
              ['Order: 14', 'canceled'],
              ['Order: 15', 'purchased']]

orders = OrderedDict(order_data)

to_move = []
to_remove = []

for key,value in orders.items():
  if value == 'returned':
    to_move.append(key)
  elif value == 'canceled':
    to_remove.append(key)

for value in to_remove:
  orders.pop(value)

for value in to_move:
  orders.move_to_end(value)

print(orders)