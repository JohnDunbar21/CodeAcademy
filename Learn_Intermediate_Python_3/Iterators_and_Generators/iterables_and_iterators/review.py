import itertools

cat_toys = [
  ("laser", 1.99),
  ("fountain", 5.99),
  ("scratcher", 10.99),
  ("catnip", 15.99)
]

max_money = 15
options = []

cat_toy_iterator = iter(cat_toys)
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

toy_combos = itertools.combinations(cat_toys, 2)

for combo in toy_combos:
    toy1 = combo[0]
    cost_of_toy1 = toy1[1]
    toy2 = combo[1]
    cost_of_toy2 = toy2[1]

    if cost_of_toy1 + cost_of_toy2 <= max_money:
      options.append(combo)

print(options)