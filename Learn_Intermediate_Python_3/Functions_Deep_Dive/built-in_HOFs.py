"""
MAP

The map() HOF has the base structure:
"""

#returned_map_object=map(function,iterable)

"""
When map() is called, it applies the function to each element in the iterable and returns a map object. The returned map object holds the
results from applying the mapping function to each element in the iterable. A map is used mainly to convert a list to enable viewing and
further use.

If we wanted to double every value in a list of numbers, you could do the following:
"""

from abc import update_abstractmethods


def double(x):
    return x*2

"""
The lambda equivalent of the double() function is:

double = lambda x: x*2
"""

int_list=[3,6,9]

doubled=map(double, int_list)
print(doubled)

"""
If we want to see the actual results of mapping double() to the elements of int_list, we need to convert the map object to a list using the
built-in list() function.
"""

print(list(doubled))

"""
HOFs work especially well with lambda functions as we don't need to define a new named function for map() if that function won't be used
again anywhere.

Writing the mapping function using a lambda is done as follows:
"""

doubled_v2=map(lambda j:j*2, int_list)
print(list(doubled_v2))

# map example:

grade_list=[3.5, 3.7, 2.6, 95, 87]

grades_100_scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list) # multiply by 25 as 100/4 = 25. 
updated_grade_list = list(grades_100_scale)
print(updated_grade_list)

"""
FILTER

The filter() function takes a function and an iterable, where the filtering function should return a boolean value.

The returned filter object will hold only those elements of the passed iterable for which the filtering function returned True.

For example:
"""

names=['margarita','Linda','Masako','Maki','Angela']
M_names=filter(lambda name: name[0] == 'M' or name[0] == 'm', names)
print(list(M_names))

# filter example:

books=[['Burgess', 1985],
['Orwell', 'Nineteen Eighty-Four'], 
['Murakami', '1Q85'], 
['Orwell', 1984], 
['Burgess', 'Nineteen Eighty-Five'], 
['Murakami', 1985]]

string_titles = filter(lambda item: type(item[1]) == str, books) # this checks if the item being iterated on is a string variable. 
string_titles_list = list(string_titles)
print(string_titles_list)

"""
REDUCE

The reduce() function has two distinct differences from map() and filter():

1. The reduce() function MUST be imported from the functools module to use it.
2. Instead of returning an object, reduce() returns a single value. This is done by reduce() applying a passed function
to each sequential pair of elements in an iterable.

For example:
"""

from functools import reduce

integer_list = [3, 6, 9, 12]
reduced_integer_list = reduce(lambda x,y: x*y, integer_list)
print(reduced_integer_list)

# reduce example:

letters = ['r', 'e', 'd', 'u', 'c', 'e']

# concatenate each letter in the letters list into one word. 
word = reduce(lambda i,j: i+j, letters) # the reduce function was already imported above. If it was not, then it would need to be imported
print(word)