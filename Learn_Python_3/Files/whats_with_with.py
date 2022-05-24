with open('fun_file.txt') as close_this_file:

    setup = close_this_file.readline()
    punchline = close_this_file.readline()

print(setup)

# Using the 'with' syntax, it removes the need to close the file after opening.
