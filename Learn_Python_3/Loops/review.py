single_digits = list(range(0, 10))

squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)

print(squares)

cubes = [num ** 3 for num in single_digits]
print(cubes)