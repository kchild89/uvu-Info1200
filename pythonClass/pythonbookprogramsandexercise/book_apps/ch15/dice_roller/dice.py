import random

class Die:
    def __init__(self):
        self.__value = 1

    @property  # read-only!
    def value(self):
        return self.__value
                
    def roll(self):
        self.__value = random.randrange(1, 7)

    # make it easier to get the value
    def __str__(self):
        return str(self.__value)
                
class Dice:
    def __init__(self):
        self.__cup = []

    def addDie(self, die):
        if not isinstance(die, Die):
            raise TypeError("die must be a Die object")
        self.__cup.append(die)
                
    def rollAll(self):
        for die in self.__cup:
            die.roll()

    def __iter__(self):
        for die in self.__cup:
            yield die
    
