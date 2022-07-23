from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

# The subplot() method can take 3 arguments: no. rows, no. columns, and the index value of the subplot. 

# subplot 1
plt.subplot(1, 2, 1)
plt.axis([0, 12, 30, 80])
plt.xlabel('Month')
plt.ylabel('Temperature in Fahrenheit')
plt.plot(months, temperature)

# subplot 2
plt.subplot(1, 2, 2)
plt.axis([30, 80, 350, 1500])
plt.xlabel('Temperature in Fahrenheit')
plt.ylabel('No. Flights To Hawaii')
plt.plot(temperature, flights_to_hawaii, marker='o', linestyle=' ')

plt.subplots_adjust(wspace=0.35)

plt.show()