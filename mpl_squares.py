import matplotlib.pyplot as plt

#styles available
"""
['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright',
'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
"""

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

#set chart and label axes

ax.set_title("Square numbers", fontsize= 24)
ax.set_xlabel("Vaule", fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)

#size of tick lables
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()
