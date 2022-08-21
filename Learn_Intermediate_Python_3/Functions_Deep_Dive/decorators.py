# 1. Functions are Objects

def add_five(num):
    print(num + 5)

add_five(3)
print(type(add_five))

# 2. Functions Within Functions

def add_five_V2(num):
    def add_two(num):
        return num + 2

    num_plus_two = add_two(num)
    print(num_plus_two + 3)

add_five_V2(4)

# 3. Returning Functions from Functions

def mathematic_operation(operator):
    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1 - num2
    
    if operator == "+":
        return add
    elif operator == "-":
        return sub

add_func = mathematic_operation("+")
print(add_func(4, 2))
sub_func = mathematic_operation("-")
print(sub_func(3, 2))

# 4. Decorating a Function

def title_decorator(print_name_function):
    def wrapper():
        print("Mr:")
        print_name_function()
    return wrapper

def print_my_name():
    print("John Dunbar")

decorated_name = title_decorator(print_my_name)

decorated_name()

# 5. Decorators

def title_decorator_V2(print_name_function):
    def wrapper():
        print("Mr:")
        print_name_function()
    return wrapper

@title_decorator
def print_my_name_V2():
    print("John Dunbar")

@title_decorator
def print_sals_name_V2():
    print("Sal Valencia")

"""
decorated_name = title_decorator(print_my_name)

decorated_name()
"""

# the above code can be executed using the @ decorator followed by the decorator function, but must be directly above the
# function that needs to be affected. 

print_my_name_V2()
print_sals_name_V2()

"""
The decorator symbol means that code can be more streamline. 
"""

# 6. Decorators w/ Parameters

def decorator(function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        function(*args, **kwargs)
    return wrapper

@decorator
def print_my_details(name, age, location):
    print(name + ", you are " + str(age) + " and are from " + location)

print_my_details("John", 22, "Aberdeen")