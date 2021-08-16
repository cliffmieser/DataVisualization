#MolecularMotion.py

"""Modfied rw_visual.py to simulaate path of pollen grain on surface of a drop of water"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walks, as long as program is active
while True:
    #make random walk

    rw = RandomWalk(5_000)
    rw.fillWalk()

    #plot points in the walk

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(15,9))
    pointNumbers = range(rw.numPoints)
    ax.plot(rw.x_values, rw.y_values, linewidth = 1)

    #emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c='red',edgecolors='none', s= 100)

    #removes axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
