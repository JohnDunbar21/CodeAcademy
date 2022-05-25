def word_length_dictionary(words):
    """Return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word."""
    length_of_words = {}
    for word in words:
        length_of_words[word] = len(word)
    return length_of_words

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}