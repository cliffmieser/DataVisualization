#die.py
from random import randint

class Die:
    """A class representing a single six sided die"""

    def __init__(self, num_sides = 6):
        """assume six sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return random value between 1 and number of sides"""
        return randint(1, self.num_sides)
