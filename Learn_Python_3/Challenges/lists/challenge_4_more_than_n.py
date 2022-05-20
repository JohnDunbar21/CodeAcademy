def more_than_n(lst, item, n):
    count = 0
    for i in lst:
        if i == item:
            count += 1
    if count > n:
        return True
    else:
        return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))