names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

name_and_heights = zip(names, heights)
print(name_and_heights) # This will print the location of the variable in the computer's memory.

converted_list = list(name_and_heights)
print(converted_list)

# When using zip, it converts list items into tuples. Converting the zipped variable into a list creates an array of tuples.

