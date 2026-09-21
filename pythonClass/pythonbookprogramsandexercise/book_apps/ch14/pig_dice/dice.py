import random
from dataclasses import dataclass

@dataclass
class Die:
    value:int = 0
                
    def roll(self):
        self.value = random.randrange(1, 7)

                
class Dice:
    # explicit constructor works better for mutable attributes
    def __init__(self):
        self.cup = []

    def addDie(self, die):
        self.cup.append(die)
                
    def rollAll(self):
        for die in self.cup:
            die.roll()
