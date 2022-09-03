"""
- Use CapWords convention when defining our namedtuple. This is because namedtuple actually returns a subclass and thus falls under the conventions we use for classes.

- The field_names argument can alternatively be a single string with each fieldname separated by whitespace and/or commas, for example, 'x y' or 'x, y'.

- At first glance, namedtuples might seem like it is trying to replicate a dictionary. While the key idea of labeling properties is the same in both structures, 
  namedtuples have some key advantages over a regular dictionary:

    - They are immutable and maintain their order, while a dictionary does not.
    
    - They are more lightweight than dictionaries and take no more memory than a regular tuple.
"""


clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

from collections import namedtuple

ClothingItem = namedtuple('ClothingItem', ['type', 'color', 'size', 'price'])

new_coat = ClothingItem('coat', 'black', 'small', 14.99)
coat_cost = new_coat[3]

updated_clothes_data = []

for item in clothes:
  updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))

print(updated_clothes_data)