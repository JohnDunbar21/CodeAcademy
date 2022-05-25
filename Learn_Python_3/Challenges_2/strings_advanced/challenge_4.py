def make_spoonerism(word1, word2):
    spoonerism1 = word2[0]+word1[1:]
    spoonerism2 = word1[0]+word2[1:]
    return "{sp1} {sp2}".format(sp1=spoonerism1, sp2=spoonerism2)

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a