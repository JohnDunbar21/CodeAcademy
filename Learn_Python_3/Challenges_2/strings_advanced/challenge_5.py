def add_exclamation(word):
    """Return a string with exclamation points up to 20 characters long in total.
    
    If the word is already longer than 20 characters, the function returns the original word."""
    while len(word) < 20: # Once the length reaches 19, the loop will append one more ! to the word and terminate. 
        word += "!"
    return word

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn