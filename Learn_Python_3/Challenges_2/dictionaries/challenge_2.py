def sum_even_keys(my_dictionary):
    """Return the sum of the even keys inside a given dictionary.
    
    This is done using the modulus."""
    count = 0 # Initialise the count variable.
    for key in my_dictionary.keys():
        if key % 2 == 0:
            count += my_dictionary[key]
    return count

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6