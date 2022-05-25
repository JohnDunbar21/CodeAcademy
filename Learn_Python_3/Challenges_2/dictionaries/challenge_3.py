def add_ten(my_dictionary):
    """Return a dictionary that takes my_dictionary as input and add 10 to every value."""
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}