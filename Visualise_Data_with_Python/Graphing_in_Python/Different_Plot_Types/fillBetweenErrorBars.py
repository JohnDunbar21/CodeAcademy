from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

y_lower = [i - (0.1 * i) for i in revenue]
y_upper = [j + (0.1 * j) for j in revenue]

plt.plot(months, revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.fill_between(months, y_lower, y_upper, alpha=0.2)
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Projected Revenue for Upcoming Financial Year')

plt.show()