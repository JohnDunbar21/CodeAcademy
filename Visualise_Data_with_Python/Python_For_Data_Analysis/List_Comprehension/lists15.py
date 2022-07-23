# The sums array returns the sum of each element from the a and b arrays combined. 
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [num1+num2 for (num1, num2) in zip(a, b)]