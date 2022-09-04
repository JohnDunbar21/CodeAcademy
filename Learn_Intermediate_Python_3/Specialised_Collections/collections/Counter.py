"""
The 'Counter' container instantly counts elements for any hashable object. 
It stores the data as a dictionary where the keys are the elements and the values are the number of occurrences.

This allows us to create a much more elegant solution without many lines of code. 

Additionally, the 'Counter' class has methods that provide further utility when working with our data. 
These methods include mathematical operations for subtracting one count dictionary from another, finding the most 
common elements, and even generating a new list of elements based on the number of occurrences.
"""


from collections import Counter

opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

def find_amount_sold(opening,closing,item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

tshirts_sold = find_amount_sold(opening_inventory, closing_inventory, 't-shirt')

print(tshirts_sold)