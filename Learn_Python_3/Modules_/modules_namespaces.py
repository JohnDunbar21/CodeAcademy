import codecademylib3_seaborn
from matplotlib import pyplot as plt 
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1, 1001), 12)

plt.plot(numbers_a, numbers_b)
plt.show()