def reversed_list(lst1, lst2):
    for item in range(len(lst1)):
        if lst1[item] != lst2[len(lst2) - 1 - item]:
            return False
    return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))