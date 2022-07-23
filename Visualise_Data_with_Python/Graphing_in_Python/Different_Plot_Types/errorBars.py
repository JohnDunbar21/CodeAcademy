from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# yerr can take a single parameter to apply to all bars, or an array to apply to each bar. 
# capsize sets the width of the top and bottom of each error bar. 

plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)

plt.show()