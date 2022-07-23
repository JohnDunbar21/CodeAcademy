from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
# plotting revenue vs time. 
plt.plot(time, revenue)
# plotting costs vs time. 
plt.plot(time, costs)
plt.show()