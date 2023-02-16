# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
#import numpy as np
from Creatures import Bear
from Creatures import Fish
import random

class River:
    
    #Initialize the river's attributes
    def __init__(self, n_room, ecosystem = [], max_periods = 5, period = 0):
        self.n_room = n_room
        self.ecosystem = ecosystem
        self.max_periods = max_periods
        self.period = period
    def initialize(self):
        for i in range(self.n_room):
            self.ecosystem.append(random.choice([Bear(), Fish(), None]))

        index = 0

        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                i.old_position = index
                i.new_position = index
            index += 1

        return self.ecosystem

    def next_time_step(self):
        self.period = self.period + 1
        print("Current period:", self.period)

        index = 0
        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                print(i.old_position)
                i.old_position = i.new_position
                i.new_position = i.old_position + i.move()
                if i.new_position <0 or i.new_position > self.n_room:
                    i.new_position = i.old_position
                print(i.new_position)

            index += 1



        print("New Ecosystem status:", self.ecosystem, "\n")

    def display(self):
        print("===================", "\n")
        print("Number of positions:", self.n_room, "\n")
        print("Ecosystem status:", self.ecosystem, "\n")
        print("===================")



