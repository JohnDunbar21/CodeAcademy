# the '*' operators is the unpacking operator in the context of function arguments. 

def print_order(*order_items):
  print(order_items)

print_order('Orange Juice','Apple Juice','Scrambled Eggs','Pancakes')