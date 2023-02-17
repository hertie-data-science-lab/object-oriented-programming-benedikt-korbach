# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta
import random

class Creature(metaclass=ABCMeta):

<<<<<<< Updated upstream
    def __init__(self, name, old_position = 0, new_position = 0): #initiate creature
        self.name = name
        self.old_position = old_position
        self.new_position = new_position
=======
    def __init__(self, name, old_position = 0, ant_position = 0, final_position = 0, moving_decision = 0): #initiate creature
        self.name = name
        self.old_position = old_position
        self.ant_position = ant_position
        self.final_position = final_position
        self.moving_decision = moving_decision
>>>>>>> Stashed changes
    def move(self):
        self.moving_decision = random.randint(-1, 1)
class Bear(Creature):
    def __init__(self, name = "Bear"):
<<<<<<< Updated upstream
        Creature.__init__(self, name, old_position = 0, new_position = 0)
        
class Fish(Creature):
    def __init__(self, name = "Fish"):
        Creature.__init__(self, name, old_position = 0, new_position = 0)
=======
        Creature.__init__(self, name, old_position = 0, ant_position = 0, final_position = 0)
        
class Fish(Creature):
    def __init__(self, name = "Fish"):
        Creature.__init__(self, name, old_position = 0, ant_position = 0, final_position = 0)
>>>>>>> Stashed changes
