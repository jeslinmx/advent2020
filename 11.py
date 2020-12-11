# Problem: https://adventofcode.com/2020/day/?

# Input
from sys import stdin
floor = [[char == "." for char in line.strip()] for line in stdin]
occupied = [[False] * len(floor[0]) for row in floor]

def state(occupied, floor):
    return "\n".join(["".join(["." if floor[y][x] else "#" if seat else "L" for x, seat in enumerate(row)]) for y, row in enumerate(occupied)])

def automaton(initial_occupied, floor, visibility_rule=False, occupy_upper_bound=0, vacate_lower_bound=4):
    from copy import deepcopy
    from itertools import product
    prev_occupied = None
    occupied = deepcopy(initial_occupied)

    while prev_occupied != occupied:
        prev_occupied = deepcopy(occupied)
        for y, row in enumerate(occupied):
            for x, _ in enumerate(row):
                if floor[y][x]:
                    continue
                if visibility_rule:
                    vicinity_occupied = 0
                    for xoffset, yoffset in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}:
                        curx, cury = x + xoffset, y + yoffset
                        while 0 <= cury < len(prev_occupied) and 0 <= curx < len(prev_occupied[0]):
                            if not floor[cury][curx]: # seat found
                                vicinity_occupied += prev_occupied[cury][curx]
                                break
                            cury += yoffset
                            curx += xoffset
                else:
                    vicinity_occupied = sum(( # equivalent to ndarray[y-1:y+1][x-1:x+1]
                        seat
                        for row in prev_occupied[max(0, y - 1):y + 2]
                        for seat in row[max(0, x - 1):x + 2]
                    )) - prev_occupied[y][x]
                if vicinity_occupied <= occupy_upper_bound:
                    occupied[y][x] = True
                elif vicinity_occupied >= vacate_lower_bound:
                    occupied[y][x] = False
    return sum((seat for row in occupied for seat in row))

# Part 1
print(automaton(occupied, floor))

# Part 2
print(automaton(occupied, floor, visibility_rule=True, vacate_lower_bound=5))