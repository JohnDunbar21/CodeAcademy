def middle_element(lst):
    if len(lst) % 2 == 0:
        middle_elem = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return middle_elem / 2
    else:
        return lst[int(len(lst)/2)]
        
# If the number of elements is even, the function will return the average of the two middle elements.

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))