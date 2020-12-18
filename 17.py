# Problem: https://adventofcode.com/2020/day/?

# Input
from sys import stdin
import numpy as np
initial = np.array([
    [char == "#" for char in line.strip()]
    for line in stdin
])

# Part 1
from itertools import product
def evolve(state, timesteps):
    if timesteps <= 0:
        return state
    # the evolution rules can be restated, in terms of nearby cubes (including
    # the target cube), as follows:
    # 1. cubes which have 3 nearby active cubes will be active, and
    # 2. currently active cubes which have 4 nearby active cubes will be active
    nearby_active = sum((
        np.pad(state, pad_width, mode="constant", constant_values=0)
        for pad_width in product([(0, 2), (1, 1), (2, 0)], repeat=state.ndim)
    ))
    next_state = (
        (nearby_active == 3) # rule 1
        | (np.pad(state, pad_width=1) & (nearby_active == 4)) # rule 2
    )
    return evolve(next_state, timesteps - 1)

print(evolve(initial[np.newaxis,:], 6).sum())

# Part 2
print(evolve(initial[np.newaxis, np.newaxis,:], 6).sum())