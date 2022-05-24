def count_char_x(word, x):
    x_count = 0
    for char in word:
        if char is x:
            x_count += 1
    return x_count

# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1