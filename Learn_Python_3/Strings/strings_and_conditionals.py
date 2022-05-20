def letter_check(word, letter):
    for char in word:
        if char == letter:
            return True
    return False