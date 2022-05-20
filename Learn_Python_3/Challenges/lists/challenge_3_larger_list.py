def larger_list(lst1, lst2):
    temp1 = len(lst1)
    temp2 = len(lst2)
    if temp1 > temp2:
        return lst1[-1]
    elif temp2 > temp1:
        return lst2[-1]
    else:
        return lst1[-1] # If both lists are the same size, return the last value of the first list.

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))