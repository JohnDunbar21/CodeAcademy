import itertools

collars = ["Red-S","Red-M", "Blue-XS", "Green-L", "Green-XL", "Yellow-M"]

collar_combo_iterator = itertools.combinations(collars, 3)

for i in collar_combo_iterator:
  print(i)

"""
The second parameter in the combinations() tool is the r-number, aka the length of each combination tuple.
"""