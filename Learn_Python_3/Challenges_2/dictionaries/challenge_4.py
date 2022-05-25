def values_that_are_keys(my_dictionary):
    """Return a list of all values in the dictionary that are also keys."""
    value_and_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_and_keys.append(value)
    return value_and_keys

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]