# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta
import random

class Creature(metaclass=ABCMeta):
    def __init__(self): #initiate creature

    def moving(self):
        move = random.randint(-1, 1)
    return move

class Bear(Creature):
    pass
 
        
class Fish(Creature):
    pass
