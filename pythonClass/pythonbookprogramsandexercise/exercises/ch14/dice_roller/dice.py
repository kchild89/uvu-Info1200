import random
from dataclasses import dataclass

@dataclass
class Die:
    __value:int = 1

    @property
    def value(self):
        return self.__value
                
    @value.setter
    def value(self, value):
        if value < 1:
            raise ValueError("Die value can't be less than 1.")
        else:
            self.__value = value
                
    def roll(self):
        self.__value = random.randrange(1, 7)

                
class Dice:
    # explicit initializer
    def __init__(self):
        self.__cup = []

    def addDie(self, die):
        self.__cup.append(die)

    @property
    def list(self):
        return tuple(self.__cup)
                
    def rollAll(self):
        for die in self.__cup:
            die.roll()
