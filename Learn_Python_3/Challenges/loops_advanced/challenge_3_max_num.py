def max_num(nums):
    current_maximum_number = nums[0]
    for num in nums:
        if current_maximum_number <= num:
            current_maximum_number = num
    return current_maximum_number

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))