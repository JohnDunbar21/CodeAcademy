from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)
plt.xlabel('Type of Coffee')
plt.ylabel('Sales Figures')
plt.title('Sales Data for Different Types of Coffee')
plt.show()