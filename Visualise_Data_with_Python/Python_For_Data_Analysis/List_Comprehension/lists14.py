# The first_only array returns the first element in each sub-list of the nested_lists array. 
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [num1 for (num1, num2) in nested_lists]