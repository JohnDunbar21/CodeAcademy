"""
Advanced Containers:

- deque
- namedtuple
- Counter
- defaultdict
- OrderedDict
- ChainMap

Container Wrappers:

- UserDict
- UserList
- UserString
"""


from collections import OrderedDict
 
orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
          'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
 
orders.move_to_end('order_4829')
orders.popitem()
print(orders)