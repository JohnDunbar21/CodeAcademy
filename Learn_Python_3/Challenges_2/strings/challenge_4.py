def substring_between_letters(word, start, end):
    start_sub_string = word.find(start)
    end_sub_string = word.find(end)
    if start_sub_string > -1 and end_sub_string > -1:
        return word[start_sub_string+1:end_sub_string]
    return word

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"