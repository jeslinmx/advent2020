# Problem: https://adventofcode.com/2020/day/15

# Input
from sys import stdin
starting_numbers = list(map(int, input().strip().split(",")))
# starting_numbers = [2,1,3]

# Part 1
from collections import deque
from itertools import count
numbers = deque(starting_numbers)
last_seen = dict(zip(starting_numbers[:-1], count())) # ignore the last number
while len(numbers) < 30000000:
    next_value = len(numbers) - 1 - last_seen[numbers[-1]] if numbers[-1] in last_seen else 0
    last_seen[numbers[-1]] = len(numbers) - 1
    numbers.append(next_value)
print(numbers[2020-1])

# Part 2
print(numbers[-1])