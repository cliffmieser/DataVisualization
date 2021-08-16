#random_walk.py

from random import choice

class RandomWalk:
    """ A class to generate random walks."""

    def __init__(self, numPoints = 5000):
        """Initialie attributes of a walk"""
        self.numPoints = numPoints

        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fillWalk(self):
        """Calculate all points in the walk"""

        #Keep tracking steps until the walk reaches desired length
        while len(self.x_values) < self.numPoints:
            #Decide which direction to go and how far in that direction
            x_direction = choice([1,-1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance        

            #reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            

            self.y_values.append(y)


