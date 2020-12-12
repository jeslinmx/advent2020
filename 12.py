# Problem: https://adventofcode.com/2020/day/12

# Input
from sys import stdin
instructions = [(line[0], int(line[1:])) for line in stdin]

# Part 1
x, y, d = 0, 0, 0
for action, amount in instructions:
    if action in ("S", "W", "R"):
        amount *= -1
    if action in ("N", "S"):
        y += amount
    elif action in ("E", "W"):
        x += amount
    elif action in ("L", "R"):
        d += amount
        d %= 360
    else:
        x += amount if d == 0 else -amount if d == 180 else 0
        y += amount if d == 90 else -amount if d == 270 else 0
print(abs(x)+abs(y))

# Part 2
x, y, wx, wy = 0, 0, 10, 1
for action, amount in instructions:
    if action in ("S", "W", "R"):
        amount *= -1
    if action in ("N", "S"):
        wy += amount
    elif action in ("E", "W"):
        wx += amount
    elif action in ("L", "R"):
        amount %= 360
        wx, wy = (wx, wy) if amount == 0 else (-wy, wx) if amount == 90 else (-wx, -wy) if amount == 180 else (wy, -wx)
    else:
        x += wx * amount
        y += wy * amount
print(abs(x)+abs(y))