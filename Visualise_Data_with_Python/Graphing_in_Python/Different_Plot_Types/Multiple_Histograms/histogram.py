from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2

plt.hist(sales_times1, bins=20,alpha=0.4)
plt.hist(sales_times2, bins=20,alpha=0.4)
# normed=True parameter not working as of the writing of this code

# Normalizing is dividing the height of each column by a constant such that the area under the curve sums to 1

plt.show()