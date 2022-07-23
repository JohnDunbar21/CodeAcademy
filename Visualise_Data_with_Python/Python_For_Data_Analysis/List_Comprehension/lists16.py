# The quotients array returns a list of num2/num1 for each item in the a and b arrays. 
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [num2/num1 for (num1, num2) in zip(a, b)]