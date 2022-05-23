available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

try:
    health_points += available_items.pop("stamina grains", 15)
except KeyError:
    health_points += 0

try:
    health_points += available_items.pop("power stew", 30)
except KeyError:
    health_points += 0

try:
    health_points += available_items.pop("mystic bread", 0)
except KeyError:
    health_points += 0

print(available_items)
print(health_points)