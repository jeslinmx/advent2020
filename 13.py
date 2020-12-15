# Problem: https://adventofcode.com/2020/day/13

# Input
earliest = int(input())
buses = input().split(",")

# Part 1
from math import prod
print(
    prod(
        min(
            (
                (int(bus) - earliest % int(bus), int(bus))
                for bus in buses
                if bus != "x"
            )
        )
    )
)

# Part 2
# for any 2 bus IDs x and y, 
print()