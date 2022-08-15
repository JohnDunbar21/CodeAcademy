"""
A lambda function (aka an anonymous function) is a one-line shorthand for-function.

For example, take a function called add_two():
"""

def add_two(my_input):
    return my_input + 2

"""
This function can be rewritten as the lambda function:
"""

addTwo = lambda my_input: my_input + 2

print(addTwo(3))
print(addTwo(100))
print(addTwo(-2))

"""
The 'lambda' keyword defines a lambda function/anonymous function, similarly to the 'def' keyword in a normal function.

Lambda functions does not require the explicit use of the 'return' keyword.
"""

"""
We can also have lambda functions that can perform conditional logic.

For example, take the function check_if_A_grade that outputs 'Got an A!' if a grade is >= 90, else outputs 'Did not get an A.'.
"""

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

print(check_if_A_grade(91))
print(check_if_A_grade(70))
print(check_if_A_grade(20))

"""
Lambda functions are the preferred way of creating one-line functions as the reduced syntax assists with code readability and can be
implemented where code reuse is not the primary objective.

If we wanted our function complexity to extend beyond one line, a normal function would be used.
"""