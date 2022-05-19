sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for scoop in location:
        scoops_sold += scoop

print(scoops_sold)