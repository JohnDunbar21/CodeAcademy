from matplotlib import pyplot as plt

x = [1, 2, 3, 4] # number of weeks
y1 = [3, 5, 1, 7] # week 1 data
y2 = [4, 8, 4, 2] # week 2 data
legend_labels = ['Week 1 Data','Week 2 Data']
plt.plot(x, y1, color='blue', marker='o')
plt.plot(x, y2, color='red', marker='o')

plt.title('Number of Days Practicing Programming in May')
plt.xlabel('Week')
plt.ylabel('Number of Days')
plt.legend(legend_labels,loc=1)

sub_plot = plt.subplot()
sub_plot.set_xticks(x)

plt.show()