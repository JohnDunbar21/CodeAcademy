"""
FUNCTIONS AS FIRST-CLASS OBJECTS

All functions are classified as first-class objects. These FCOs have four important characteristics:

1. FCOs can be stored as variables.
2. FCOs can be passed as arguments to a function.
3. FCOs can be returned by a function.
4. FCOs can be stored in a data structure (e.g., lists, dictionaries, etc).

FCOs allow us to write functions called Higher-Order Functions.

A HOF operates on other functions via arguments or via return values. This means that HOFs do one or both
of the following:

- Accept a function as an argument.
- Have a return value that is a function.

"""

"""
FUNCTIONS AS ARGUMENTS

Examine the HOF called total_bill():
"""

def total_bill(func,value):
    total=func(value)
    return total

"""
The total_bill function takes 2 arguments: func and value. When called, the function applies func() to value and returns the result.

To see it in action, let us define a function called add_tax(), then pass it into our total_bill function.
"""

def add_tax(total):
    tax=total*0.06
    new_total=total+tax
    return new_total

total_bill(add_tax, 100)

"""
The total_bill function is the HOF in this example as it takes a function as an argument.

Let's reuse our HOF to add a 20% gratuity instead of a 6% sales tax:
"""

def add_tip(total):
    tip=total*0.2
    new_total=total+tip
    return new_total

total_bill(add_tip, 100)

"""
The appeal of HOFs comes when we want to keep consistent manipulation no matter what function is passed in.

We can modify total_bill so it formats our total amount in a user-friendly and consistent way, regardless of the function passed in.
"""

def new_total_bill(func,value):
    total=func(value)
    return ("The total amount owed is $"+"{:.2f}".format(total)+". Thank you!")

print(new_total_bill(add_tax, 100))
print(new_total_bill(add_tip, 100))

"""
HOFs make code more modular and maintainable.
"""

"""
FUNCTIONS AS ARGUMENTS - ITERATION

If you have a set of values that need processing, you can process them in a loop and add them to a new list as shown below:
"""

bills=[115,120,42]
new_bills=[]
for i in range(len(bills)):
    total=add_tax(bills[i])
    new_bills.append(("Total amount owed is $"+"{:.2f}".format(total)+". Thank you!"))

print(new_bills)

"""
A much more effective solution would be to define a HOF which can take a function and a list in this instance to prevent repetitive
code in the program.
"""

def hof_total_bills(func, list):
    new_bills=[]
    for i in range(len(list)):
        total=func(list[i])
        new_bills.append("Total amount owed is $"+"{:.2f}".format(total)+". Thank you!")
    return new_bills

bills_w_tax = hof_total_bills(add_tax, bills)
print(bills_w_tax)
bills_w_tips = hof_total_bills(add_tip, bills)
print(bills_w_tips)

"""
FUNCTIONS AS RETURN VALUES

A function that returns another function is also a HOF.

Let's define a function that finds the volume of a box.
"""

def box_volume(height):

    def volume(length, width):
        return length*width*height

    return volume

box_vol_height_15 = box_volume(15)
print(box_vol_height_15(3,2))
box_vol_height_10 = box_volume(10)
print(box_vol_height_10(3,2))