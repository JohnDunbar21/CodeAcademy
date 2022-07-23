from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

# you can define axis boundaries: in this case, the x-axis runs from 0-12, and the y-axis runs from 2900-3100. 
plt.axis([0, 12, 2900, 3100])
plt.show()