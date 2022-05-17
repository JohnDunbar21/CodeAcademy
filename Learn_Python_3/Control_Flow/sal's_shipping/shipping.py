weight = 10
premium_ground_shipping = 125.00

# Ground shipping
if weight <= 2.0:
  print(20.00 + (weight * 1.5))
elif weight > 2.0 and weight <= 6.0:
  print(20.00 + (weight * 3.0))
elif weight > 6.0 and weight <= 10.0:
  print(20.00 + (weight * 4.0))
elif weight > 10.0:
  print(20.00 + (weight * 4.75))

print(premium_ground_shipping)

# Drone shipping
if weight <= 2.0:
    print(weight * 4.5)
elif weight > 2.0 and weight <= 6.0:
    print(weight * 9.0)
elif weight > 6.0 and weight <= 10.0:
    print(weight * 12.0)
elif weight > 10.0:
    print(weight * 14.25)