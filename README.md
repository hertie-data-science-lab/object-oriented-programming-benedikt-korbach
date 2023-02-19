Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish died (i.e., it disappears).


Our Assumptions:

- Before the first period begins, the ecosystem is initialized. The number of positions in the river can be chosen freely.
- Also, the number of periods can be chosen.

- At the beginning of each period, we anticipate the movement of the animals.
- If several animals are anticipated to collide in one or several positions, we resolve the collisions sequentially (starting from the most "upstream" position, e.g. position collision at position 1 will be resolved before position 6)
    - a) If animals of the same kind collide, the animals stay at their position at the beginning of the period and "1" will be added to the animal specific spawn counter (e.g. two bears collide, the bear_spawn_counter increases by one)
        - If three bears or fish collide in the same position, the animal specific spawn counter will only increase by one.
    - b) If a bear and a fish or several bear and fish collide in one position, the bear(s) kill(s) all the fish (anticipated position of the fish = None) and move(s) to this position.
        - If several bears are present in the position, they will collide in the next round of collisions as indicated in a)
- After clearing all the collisions, new animals will spawn at random empty positions of the river (one animal, fish or bear, per same animal collision).
    - If there are not enough empty positions, the empty positions will be filled until all positions of the ecosystem are occupied.
    - If there are both fish and bears are supposed to spawn due to same animal collisions within one period, fish are priritzed with respect to bears. (e.g. only one empty position and one fish and one bear are supposed to spawn, only the fish spawns in the empty position).


Group Members:

Benedikt Korbach - 221136 

Alvaro Guijarro - 266883
