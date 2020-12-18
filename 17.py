# Problem: https://adventofcode.com/2020/day/?

# Input
from sys import stdin
initial = [
    (y, x)
    for y, line in enumerate(stdin)
    for x, char in enumerate(line.strip())
    if char == "#"
]

# Part 1
from operator import add
from itertools import product
from collections import defaultdict
def evolve(points, timesteps):
    if timesteps <= 0:
        return points
    nearby_active = defaultdict(int)
    for point in points:
        for offset in product([-1, 0, 1], repeat=len(point)):
            nearby_active[tuple(map(add, point, offset))] += 1
    # the evolution rules can be restated, in terms of nearby cubes (including
    # the target cube), as follows:
    # 1. cubes which have 3 nearby active cubes will be active, and
    # 2. currently active cubes which have 4 nearby active cubes will be active
    next_state = [
        point
        for point, nearby in nearby_active.items()
        if nearby == 3 or (point in points and nearby == 4)
    ]
    return evolve(next_state, timesteps - 1)

initial_cube = [(0, y, x) for y, x in initial]
print(len(evolve(initial_cube, 6)))

# Part 2
initial_hypercube = [(0, 0, y, x) for y, x in initial]
print(len(evolve(initial_hypercube, 6)))