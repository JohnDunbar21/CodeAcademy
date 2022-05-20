def win_percentage(wins, losses):
    total = wins + losses
    return ((wins/total) * 100)

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100