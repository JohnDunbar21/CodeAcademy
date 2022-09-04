"""
Dictionaries are another popular type of collection we use in our programs. 
Although they are great for a lot of situations, applications that rely heavily on them always run into a common issue. 
This issue deals with how to handle missing keys!

When we try to access a key-value pair in a dictionary, but the key does not exist, a dictionary will normally throw a 'KeyError'.

We set the default value using a lambda expression.
Any time we try to access a key that does not exist, it automatically updates our 'defaultdict' object by creating the new key-value 
pair using the missing key and the default value.
"""


site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

from collections import defaultdict

validated_locations = defaultdict(lambda: 'TODO: Add to website')

validated_locations.update(site_locations)

for item in updated_products:
  site_locations[item] = validated_locations[item]

print(site_locations)