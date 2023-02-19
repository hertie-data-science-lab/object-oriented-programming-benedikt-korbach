# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""

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
                print("Beginning of period position of", i, ":", i.old_position)
                i.move()
                print("Moving decision:", i.moving_decision)
                i.ant_position = i.old_position + i.moving_decision
                # Prevent animals to move out of the boundaries of the ecosystem
                if i.ant_position < 0 or i.ant_position >= self.n_room:
                    i.ant_position = i.old_position
                print("Anticipated position of", i, ":", i.ant_position, "\n")
        print("===================", "\n")

    # Check for anticipated collisions and save final moving results in final_position of each animal
    def collisions(self):
        collision_list = []
        index_list = []
        tuple_list = []

        # Find positions of the river where collisions are anticipated; append these positions to the collision_list
        for i in self.ecosystem:
            if isinstance(i, Fish) or isinstance(i, Bear):
                if i.ant_position in index_list:
                    if i.ant_position not in collision_list:
                        collision_list.append(i.ant_position)
                tuple_list.append((i.ant_position, i))
                index_list.append(i.ant_position)

        for animal in tuple_list:
            animal[1].final_position = animal[1].ant_position

        print("Animal positions: ", index_list)
        print("Collisions at position(s): ", collision_list)
        print("Animals and their positions:", tuple_list, "\n")

        # Resolve all collisions as long as there are collision as indicated by the collision_list
        while len(collision_list) != 0:
            for animal in tuple_list:
                animal[1].final_position = animal[1].ant_position

            # Save the animals taking part in a collision in the interaction_list
            for i in collision_list:
                interaction_list = []
                for t in tuple_list:
                    if t[0] == i:
                        interaction_list.append(t[1])
                print("Collision at position:", i)
                print("Animals colliding:", interaction_list, "\n")

                # If animals of the same kind collide (bear and bear, fish and fish), set ant_position to old_position for each animal and increase the spawn_counter by one
                if all(isinstance(animal, type(interaction_list[0])) for animal in interaction_list):
                    for animal in interaction_list:
                        animal.ant_position = animal.old_position
                        print("Animal: ", animal)
                        print("Beginning of period position: ", animal.old_position)
                        print("New anticipated position: ", animal.ant_position, "\n")
                    if isinstance(interaction_list[0], Fish):
                        self.fish_spawn_counter += 1
                    else:
                        self.bear_spawn_counter += 1

                # If animals of different kinds collide (bear and fish), set the anticipated_position of the fish to NONE and the anticipated position of the bear to the position where the collision took place
                else:
                    for animal in interaction_list:
                        if isinstance(animal, Fish):
                            animal.ant_position = None
                            print("Animal: ", animal)
                            print("Beginning of period position: ", animal.old_position)
                            print("New anticipated position: ", animal.ant_position, "\n")
                        if isinstance(animal, Bear):
                            print("Animal: ", animal)
                            print("Beginning of period position: ", animal.old_position)
                            print("New anticipated position: ", animal.ant_position, "\n")

            #Reset list
            collision_list = []
            index_list = []
            tuple_list = []

            # Check for secondary (tertiary, etc,) collisions; find positions of the river where collisions are anticipated
            for i in self.ecosystem:
                if isinstance(i, Fish) or isinstance(i, Bear):
                    if i.ant_position is not None:
                        if i.ant_position in index_list:
                            if i.ant_position not in collision_list:
                                collision_list.append(i.ant_position)
                    tuple_list.append((i.ant_position, i))
                    index_list.append(i.ant_position)

            print("After collision status: ")
            print("Animal positions: ", index_list)
            print("Collisions at position(s): ", collision_list)
            print("After collision animal positions : ", tuple_list, "\n")

            for animal in tuple_list:
                animal[1].final_position = animal[1].ant_position

    # Method to spawn animals as a result of collision of the same kinds of animals
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


        print("Fish to spawn: ", self.fish_spawn_counter)
        print("Bears to spawn: ", self.bear_spawn_counter)

        none_index_list = []

        for i in range(self.n_room):
            if self.ecosystem[i] is None:
                none_index_list.append(i)

        print("Free positions: ", none_index_list)

        free_none_spots = len(none_index_list)

        print("Number of free positions: ", free_none_spots, "\n")

        # Spawn animals if there are still empty positions in the ecosystem. Prioritize fish over bears
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

        print("Final ecosystem status of the period:", self.ecosystem, "\n")

        self.fish_spawn_counter = 0
        self.bear_spawn_counter = 0

    # Aggregate methods as next_time_step
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
        print("===================", "\n")


