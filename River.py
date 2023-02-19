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
    
    def __init__(self, n_room, ecosystem = [], period = 0, fish_spawn_counter = 0, bear_spawn_counter = 0):
        self.n_room = n_room
        self.ecosystem = ecosystem
        self.period = period
        self.fish_spawn_counter = fish_spawn_counter
        self.bear_spawn_counter = bear_spawn_counter

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
        print("Anticipated moves:", "\n")
        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                print("Old position of ", i, " :", i.old_position)
                i.move()
                print("Moving decision: ", i.moving_decision)
                i.ant_position = i.old_position + i.moving_decision
                if i.ant_position < 0 or i.ant_position >= self.n_room:
                    i.ant_position = i.old_position
                print("Anticipated position of ", i, " :", i.ant_position, "\n")
        print("===================", "\n")

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

        #List to check the steps
        #print("index_list: ", index_list) #Index list of river positions with bears or fishes
        #print("collision_list: ", collision_list) #Index list of positions were a collision happened
        #print("tuple_list: ", tuple_list, "\n") #Tuple with index and type of creature in the ecosystem

        for animal in tuple_list:
            animal[1].final_position = animal[1].ant_position

        while len(collision_list) != 0:
            for animal in tuple_list:
                animal[1].final_position = animal[1].ant_position

            for i in collision_list:
                interaction_list = []
                for t in tuple_list:
                    if t[0] == i:
                        interaction_list.append(t[1])
                print("Collision at position :", i)
                print("interaction_list =", interaction_list, "\n")

                # If animals of the same kind collide, set ant position to old position
                if all(isinstance(animal, type(interaction_list[0])) for animal in interaction_list):
                    for animal in interaction_list:
                        animal.ant_position = animal.old_position
                        print("Animal: ", animal)
                        print("Old position: ", animal.old_position)
                        print("Ant position: ", animal.ant_position, "\n")
                    if isinstance(interaction_list[0], Fish):
                        self.fish_spawn_counter += 1
                    else:
                        self.bear_spawn_counter += 1

                # If animals of different kinds collide, therefore bear and fish, set the ant_position of the fish to NONE
                else:
                    for animal in interaction_list:
                        if isinstance(animal, Fish):
                            animal.ant_position = None
                            print("Animal: ", animal)
                            print("Old position: ", animal.old_position)
                            print("Ant position: ", animal.ant_position, "\n")
                        if isinstance(animal, Bear):
                            print("Animal: ", animal)
                            print("Old position: ", animal.old_position)
                            print("Ant position: ", animal.ant_position, "\n")

            #Reset list
            collision_list = []
            index_list = []
            tuple_list = []

            # Find positions of the river where collisions are anticipated
            for i in self.ecosystem:
                if isinstance(i, Fish) or isinstance(i, Bear):
                    if i.ant_position is not None:
                        if i.ant_position in index_list:
                            if i.ant_position not in collision_list:
                                collision_list.append(i.ant_position)
                    tuple_list.append((i.ant_position, i))
                    index_list.append(i.ant_position)

            print("Check ecosystem update: ")
            print("Index_list: ", index_list)
            print("Collision_list: ", collision_list)
            print("Tuple_list: ", tuple_list, "\n")

            for animal in tuple_list:
                animal[1].final_position = animal[1].ant_position


    def update_ecosystem(self):
        print("Old ecosystem status :", self.ecosystem)
        new_ecosystem = [None] * self.n_room

        for i in self.ecosystem:
            if i is not None:
                if i.final_position is not None:
                    new_ecosystem[i.final_position] = i
                i.old_position = i.final_position

        self.ecosystem = new_ecosystem
        print("New ecosystem status :", self.ecosystem, "\n")
        print("fish_spawn_counter: ", self.fish_spawn_counter)
        print("bear_spawn_counter: ", self.bear_spawn_counter)

        none_index_list = []

        for i in range(self.n_room):
            if self.ecosystem[i] is None:
                none_index_list.append(i)

        print("none_index_list: ", none_index_list)

        free_none_spots = len(none_index_list)

        print("free_none_spots: ", free_none_spots, "\n")

        for i in range(self.fish_spawn_counter):
            if free_none_spots > 0:
                index_position = random.choice(none_index_list)
                self.ecosystem[index_position] = Fish()
                self.ecosystem[index_position].old_position = index_position
                self.ecosystem[index_position].ant_position = index_position
                self.ecosystem[index_position].final_position = index_position
                print(self.ecosystem[index_position], "spawns in position", index_position, "\n")

                none_index_list.remove(index_position)
            free_none_spots -= 1

        for i in range(self.bear_spawn_counter):
            if free_none_spots > 0:
                index_position = random.choice(none_index_list)
                self.ecosystem[index_position] = Bear()
                self.ecosystem[index_position].old_position = index_position
                self.ecosystem[index_position].ant_position = index_position
                self.ecosystem[index_position].final_position = index_position
                print(self.ecosystem[index_position], "spawns in position", index_position, "\n")

                none_index_list.remove(index_position)
            free_none_spots -= 1

        print("New ecosystem status :", self.ecosystem, "\n")

        self.fish_spawn_counter = 0
        self.bear_spawn_counter = 0



    # Aggragate methods as next_time_step
    def next_time_step(self):
        self.period = self.period + 1
        print("Current period:", self.period, "\n")
        self.anticipated_moves()
        self.collisions()
        self.update_ecosystem()
        print("===================", "\n")

    def display(self):
        print("===================", "\n")
        print("Number of positions:", self.n_room, "\n")
        print("Ecosystem status:", self.ecosystem, "\n")
        print("===================")


