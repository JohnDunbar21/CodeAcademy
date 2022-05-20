def larger_sum(lst1, lst2):
    sum_lst1 = 0
    sum_lst2 = 0
    for item in lst1:
        sum_lst1 += item
    for item in lst2:
        sum_lst2 += item
    if sum_lst1 > sum_lst2:
        return lst1
    elif sum_lst2 > sum_lst1:
        return lst2
    elif sum_lst1 == sum_lst2:
        return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))