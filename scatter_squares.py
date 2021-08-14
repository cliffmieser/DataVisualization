#scatter_squares.py
import matplotlib.pyplot as plt

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200) # 's' sets the size of the dot in this scatter method

#set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Size set for tick labels
ax.tick_params(axis = 'both', which = 'major', labelsize =14)


plt.show()
