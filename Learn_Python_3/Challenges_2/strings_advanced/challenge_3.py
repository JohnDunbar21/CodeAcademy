def reverse_string(word):
    reverse = ""
    for item in range(len(word)-1, -1, -1):
        reverse += word[item]
    return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print