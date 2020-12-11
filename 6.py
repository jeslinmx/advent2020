# Problem: https://adventofcode.com/2020/day/6

# Input
from sys import stdin
groups = "".join(stdin).split("\n\n")

# Part 1
print(
    sum([
        len(set(group) - {"\n", " "}) # number of unique (non-blank) chars
        for group in groups
    ])
)

# Part 2
print(
    sum([
        len(set.intersection(*[
            set(person)
            for person in group.replace("\n", " ").split()
        ]))
        for group in groups
    ])
)