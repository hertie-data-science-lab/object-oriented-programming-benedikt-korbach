# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta
import random

class Creature(metaclass=ABCMeta):

    def __init__(self, name, old_position = 0, new_position = 0, final_position = 0): #initiate creature
        self.name = name
        self.old_position = old_position
        self.new_position = new_position
        self.final_position = final_position
    def move(self):
        return random.randint(-1, 1)
class Bear(Creature):
    def __init__(self, name = "Bear"):
        Creature.__init__(self, name, old_position = 0, new_position = 0, final_position = 0)
        
class Fish(Creature):
    def __init__(self, name = "Fish"):
        Creature.__init__(self, name, old_position = 0, new_position = 0, final_position = 0)
