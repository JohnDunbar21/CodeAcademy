def unique_values(my_dictionary):
    """Return a number which is the count of all values from the dictionary without including duplicates."""
    unique_values = []
    for value in my_dictionary.values():
        if value not in unique_values:
            unique_values.append(value)
    return len(unique_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1