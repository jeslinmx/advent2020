# Problem: https://adventofcode.com/2020/day/14

# Input
from sys import stdin
program = list(stdin)

# Part 1
from collections import defaultdict
mem = defaultdict(int)
for line in program:
    if line.startswith("mask = "):
        mask = line.strip()[-36:]
        ones_mask = int(mask.replace("X", "0"), base=2)
        zeroes_mask = int(mask.replace("X", "1"), base=2)
    else:
        address, value = line[4:].split("] = ")
        # override ones using OR, and override zeroes using AND
        mem[int(address)] = (int(value) | ones_mask) & zeroes_mask
print(sum(mem.values()))

# Part 2
from itertools import product
mem = defaultdict(int)
for line in program:
    if line.startswith("mask = "):
        mask = line.strip()[-36:]
        ones_mask = int(mask.replace("X", "0"), base=2)
        floating_mask = int(mask.replace("0", "1").replace("X", "0"), base=2)
        floating_values = [
            (0, 1 << position)
            for position, char in enumerate(reversed(mask))
            if char == "X"
        ]
    else:
        address, value = line[4:].split("] = ")
        # override ones, and override floating bits to zeroes
        base_address = (int(address) | ones_mask) & floating_mask
        for floating_value in product(*floating_values):
            mem[base_address + sum(floating_value)] = int(value)
print(sum(mem.values()))