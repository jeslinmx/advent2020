# Problem: https://adventofcode.com/2020/day/3

# Input
from sys import stdin
trees = [[char == "#" for char in line.strip()] for line in stdin]

# Part 1
from itertools import count
def collisions(right, down):
    return sum([
        trees[row][col % len(trees[0])]
        for row, col in zip(range(down, len(trees), down), count(right, right))
    ])
print(collisions(3, 1))

# Part 2
from math import prod
print(prod([
    collisions(*slope) for slope in ((1,1), (3,1), (5,1), (7,1), (1,2))
]))