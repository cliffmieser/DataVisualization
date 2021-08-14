#cubes_exercise

#A graph plotting the first 5000 numbers raised by the third power
#Applies colormap to cubes plot

import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Blues, s = 10)

ax.set_title("Cube Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of value", fontsize = 14)

ax.tick_params(axis='both', which='major', labelsize=14)




plt.show()

