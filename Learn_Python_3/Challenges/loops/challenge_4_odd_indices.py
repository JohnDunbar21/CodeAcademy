def odd_indices(lst):
    new_list = []
    for item in range(1, len(lst), 2):
        new_list.append(lst[item])
    return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))