import itertools

max_capacity = 1000
num_bags = 0

for i in itertools.count(start=13.5, step=13.5):
  if i >= max_capacity:
    break
  num_bags += 1

print(num_bags)