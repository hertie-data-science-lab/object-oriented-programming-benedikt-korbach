Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish died (i.e., it disappears).

Assumptions:

-We first anticipate all the movements and then clear the collisions sequentially

-There might be animals involved in different collision in each round, depending on the sequential order that collisions are resolved

-If there are no available empty spots, collisions between same type of animals will not spawn a new one

-The simulation will go as far as the number of round stated in the main.py 

Group Members:
Benedikt Korbach - 221136 

Alvaro Guijarro - 266883
