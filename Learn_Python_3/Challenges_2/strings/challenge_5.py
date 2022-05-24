def x_length_words(sentence, x):
    num_words = sentence.split(" ")
    for item in num_words:
        if len(item) < x:
            return False
    return True

# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True