def sum_values(my_dictionary):
    """Returns the sum of the values contained inside a dictionary."""
    count = 0 # Initialise the count variable.
    for value in my_dictionary.values():
        count += value
    return count

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6