def same_values(lst1, lst2):
    new_list = []
    for item in range(len(lst1)):
        if lst1[item] == lst2[item]:
            new_list.append(item)
    return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))