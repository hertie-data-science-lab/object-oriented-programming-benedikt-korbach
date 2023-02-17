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
    
    def __init__(self, n_room, ecosystem = [], max_periods = 5, period = 0):
        self.n_room = n_room
        self.ecosystem = ecosystem
        self.max_periods = max_periods
        self.period = period

    def initialize(self):
        # Randomly assign a bear, a fish or NONE to each position in the river
        for i in range(self.n_room):
            self.ecosystem.append(random.choice([Bear(), Fish(), None]))

        # Change old_position, ant_position and final_position to position of animal in the river
        index = 0

        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                i.old_position = index
                i.ant_position = index
                i.final_position = index

            index += 1

        return self.ecosystem

    # Make creatures move and save result in anticipated position attribute of each animal
    def anticipated_moves(self):
        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                print("Old position of ", i, " :", i.old_position)
                i.move()
                print("Moving decision: ", i.moving_decision)
                i.ant_position = i.old_position + i.moving_decision
                if i.ant_position < 0 or i.ant_position >= self.n_room:
                    i.ant_position = i.old_position
                print("Anticipated position of ", i, " :", i.ant_position, "\n")

    # Check for anticipated collisions and save final moving results in final_position
    def collisions(self):
        collision_list = []
        index_list = []
        tuple_list = []

        # Find positions of the river where collisions are anticipated
        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                if i.ant_position in index_list:
                    if i.ant_position not in collision_list:
                        collision_list.append(i.ant_position)
                tuple_list.append((i.ant_position, i))
                index_list.append(i.ant_position)

        print("index_list: ", index_list)
        print("collision_list: ", collision_list)
        print("tuple_list: ", tuple_list)

        while len(collision_list) != 0:
            for animal in tuple_list:
                animal[1].final_position = animal[1].ant_position

            for i in collision_list:
                interaction_list = []
                for t in tuple_list:
                    if t[0] == i:
                        interaction_list.append(t[1])
                print("interaction_list =", interaction_list)

                # If animals of the same kind collide, set ant position to old position
                if all(isinstance(animal, type(interaction_list[0])) for animal in interaction_list):
                    for animal in interaction_list:
                        print("Animal: ", animal)
                        print("Old position: ", animal.old_position)
                        print("Ant position: ", animal.ant_position)

                        animal.ant_position = animal.old_position
                # If animals of different kinds collide, therefore bear and fish, set the ant_position of the fish to NONE
                else:
                    for animal in interaction_list:
                        if isinstance(animal, Fish):
                            animal.ant_position = None
                            print("Animal: ", animal)
                            print("Old position: ", animal.old_position)
                            print("Ant position: ", animal.ant_position)
                        if isinstance(animal, Bear):
                            animal.ant_position = animal.old_position
                            print("Animal: ", animal)
                            print("Old position: ", animal.old_position)
                            print("Ant position: ", animal.ant_position)

            collision_list = []
            index_list = []
            tuple_list = []

            # Find positions of the river where collisions are anticipated
            for i in self.ecosystem:
                if isinstance(i, Fish) or isinstance(i, Bear):
                    if i.ant_position in index_list:
                        if i.ant_position not in collision_list:
                            collision_list.append(i.ant_position)
                    index_list.append(i.ant_position)

            print("index_list: ", index_list)
            print("collision_list: ", collision_list)

    def null_positions(self):
        #Identify after the creature's movement which are the null positions in the river
        null_positions = []
        for i in range(self.n_room):
            if self.ecosystem[i] is None:
                null_positions.append(i)
        print("This are the null positions",null_positions)

        #Iteraction between creatures

        print("New Ecosystem status:", self.ecosystem, "\n")


    # Aggragate methods as next_time_step
    def next_time_step(self):
        self.period = self.period + 1
        print("Current period:", self.period, "\n")
        self.anticipated_moves()
        self.collisions()

    def display(self):
        print("===================", "\n")
        print("Number of positions:", self.n_room, "\n")
        print("Ecosystem status:", self.ecosystem, "\n")
        print("===================")


