# Water-Sorted-Tuple-Game
The game consists of a number of bottles, full of layers of different colored bottles, and generally one or two empty bottles, and the goal is to make all bottles uniformly colored. A move consists of taking a bottle full of at least one layer and pouring it into another bottle. 

![image](https://github.com/hazalnurasma/sorted-tuple-game/assets/16530226/121dab6b-1648-4b6d-9311-170638b12e83)

Rules
------

-You can only move the top most color from one container to another.

-You can only move a color into a container if the top most color is the same, unless the container is empty.

-You can only move a color into a container that is not already at its maximum capacity

-If there are multiple concurrent items of the same color in the source container, all will be transferred to the destination container until it reaches it's maximum capacity, this means if the empty space in the destination container is not equal to the source concurrent items swap transfer will not be executed.

Implementation
------
As a basis, the method of Raymond Hettinger's Generic Puzzle Solver is used by depth-first search algorithm.

![image](https://github.com/hazalnurasma/sorted-tuple-game/assets/16530226/df61f0c7-a6fd-4fd6-99a7-822d88d11b2f)


The core idea while we develop our algorithm is that we need very few things to describe the puzzle in a way that a solver can find a solution:

1)We need an initial position (the unsolved puzzle)

2)We need a rule (typically an iterator) to generate all possible moves from a position.

3)We need to recognize the goal state.

**You can reach the final version of this project to algorithm_4_working.py file.**



