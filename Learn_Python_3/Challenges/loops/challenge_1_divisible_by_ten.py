def divisible_by_ten(nums):
    count = 0
    for num in nums:
        if num % 10 == 0:
            count += 1
        else:
            pass
    return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))