# Problem: https://adventofcode.com/2020/day/16

# Input
from sys import stdin
import re
puzzle_input = [line.strip() for line in stdin]

rules = {
    rule[1]: ((int(rule[2]), int(rule[3])), (int(rule[4]), int(rule[5])))
    for rule in (
        re.fullmatch(r"(.+): (\d+)-(\d+) or (\d+)-(\d+)", line)
        for line in puzzle_input[0:(puzzle_input.index("your ticket:") - 1)]
    )
}

my_ticket = list(map(int, puzzle_input[puzzle_input.index("your ticket:") + 1].split(",")))

nearby = [
    list(map(int, line.split(",")))
    for line in puzzle_input[(puzzle_input.index("nearby tickets:") + 1):]
]

# Part 1
from bisect import bisect_left, bisect_right
class Multiinterval(object):
    def __init__(self, points=[float("-inf")]):
        self.points = points
    
    def _create_new_points(self, interval):
        l = bisect_left(self.points, interval[0])
        u = bisect_right(self.points, interval[1])
        return (
            self.points[:l]
            + ([interval[0]] if l % 2 != 0 else [])
            + ([interval[1]] if u % 2 != 0 else [])
            + (self.points[u+1:] if u % 2 != 0 else self.points[u:])
        )

    def include(self, interval):
        self.points = self._create_new_points(interval)
        return self

    def __add__(self, interval):
        return Multiinterval(self._create_new_points(interval))

    def __contains__(self, value):
        return (
            # the bisect_left fails when value equals a lower bound, while the
            # bisect_right fails for an upper bound.
            (bisect_left(self.points, value) % 2 == 0) or
            (bisect_right(self.points, value) % 2 == 0)
        )

# create the union of all intervals from all rules
valid_interval = sum(
    [interval for field in rules for interval in rules[field]],
    start=Multiinterval()
)

# sum up all values which do not fall in the interval union
print(sum((
    value for ticket in nearby for value in ticket
    if value not in valid_interval
)))

# Part 2
valid_tickets = [
    ticket for ticket in nearby
    if all((value in valid_interval for value in ticket))
]

rule_intervals = {
    field: sum(intervals, start=Multiinterval())
    for field, intervals in rules.items()
}

possible_fields = [
    (set((
        field for field, interval in rule_intervals.items()
        if all((value in interval for value in [
            ticket[position] for ticket in valid_tickets
        ]))
    )), position)
    for position in range(len(valid_tickets[0]))
]

possible_fields = sorted(possible_fields, key=lambda x: len(x[0]))
accounted_fields = set()
field_columns = dict()
for fields, position in possible_fields:
    field = list(fields - accounted_fields)[0]
    field_columns[field] = position
    accounted_fields.add(field)

from math import prod

print(prod((
    my_ticket[field_columns[field]]
    for field, position in field_columns.items()
    if "departure" in field
)))