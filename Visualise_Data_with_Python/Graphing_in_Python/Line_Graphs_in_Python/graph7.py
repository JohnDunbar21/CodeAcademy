from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

# subplots_adjust():
#   - left = left-side margin, default 0.125. Can increase to make room for the y-axis label
#   - right = right-side margin, default 0.9. Can increase to make more room for figure, or decrease it to make more room for legend
#   - bottom = bottom margin, default 0.1. Can increase to make room for tick-mark or x-axis labels
#   - top = top margin, default 0.9
#   - wspace = horizontal space between adjacent subplots, default 0.2
#   - hspace = vertical space between adjacent subplots, default 0.2


plt.subplots_adjust(wspace=0.35, bottom=0.2)
plt.show()