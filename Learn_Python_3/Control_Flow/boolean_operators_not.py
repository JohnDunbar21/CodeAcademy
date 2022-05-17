statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not credits >= 120:
    print("You do not have enough credits to graduate.")
elif not gpa >= 2.0:
    print("Your GPA is not high enough to graduate.")
elif not credits >= 120 and not gpa >= 2.0:
    print("You do not meet either requirement to graduate!")