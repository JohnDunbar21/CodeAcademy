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

"""
FILTER

The filter() function takes a function and an iterable, where the filtering function should return a boolean value.

The returned filter object will hold only those elements of the passed iterable for which the filtering function returned True.

For example:
"""

names=['margarita','Linda','Masako','Maki','Angela']
M_names=filter(lambda name: name[0] == 'M' or name[0] == 'm', names)
print(list(M_names))

#continue