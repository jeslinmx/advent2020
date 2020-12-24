# Problem: https://adventofcode.com/2020/day/24

# Part 1
from sys import stdin
from collections import defaultdict
# representing the tiles with a dict mapping (x, y) coord tuples to a boolean
# (0, 0) is the reference tile; (-1, 0) is west of it, and (1, 0) is east of it
# (-0.5, -0.5) is southwest, while (0, -1) is SW then SE (or SE then SW)
# the boolean represents whether a tile is black
tiles = defaultdict(bool)
for line in stdin:
    x, y = 0, 0
    h_distance = 1
    for char in line.strip():
        if char in ("w", "e"):
            if char == "w":
                x -= h_distance
            else:
                x += h_distance
            h_distance = 1
        else:
            # char is either n or s, which means that the next char is either e
            # or w, and it only moves x by 0.5
            if char == "n":
                y += 0.5
            else:
                y -= 0.5
            h_distance = 0.5
    tiles[(x, y)] = not tiles[(x, y)]
print(sum(tiles.values()))

# Part 2
# this again?
from operator import add
directions = (
    (1, 0), # e
    (0.5, -0.5), # se
    (-0.5, -0.5), # sw
    (-1, 0), # w
    (-0.5, 0.5), # nw
    (0.5, 0.5)
)
# change our data representation into a set of coords of black tiles
black = set(filter(lambda x: tiles[x], tiles))
for _ in range(100):
    nearby_black = defaultdict(int)
    for coords in black:
        for offset in directions:
            nearby_black[tuple(map(add, coords, offset))] += 1
    flip_to_white = set([
        coords
        for coords in black
        if (
            coords not in nearby_black # black tile w/ 0 adjacent black tiles
            or nearby_black[coords] > 2 # black tile w/ >2 adjacent black tiles
        )
    ])
    flip_to_black = set([
        coords
        for coords in nearby_black
        if nearby_black[coords] == 2
    ])
    black = (black | flip_to_black) - flip_to_white
print(len(black))