my_info = ('John', 22, 'Student')
print(my_info)

print(my_info[0])
print(my_info[1])
print(my_info[-1])

# You cannot change elements inside a tuple after assigning them.

name, age, occupation = my_info
print(name)
print(age)
print(occupation)

one_element_tuple = (4,) # a comma msut be used to create a 1 element tuple.

# lists/arrays are useful when data is similar and needs to be sorted and/or mutated in some way.
# Tuples are useful when data is not similar, but needs to be grouped together in a specific order.
