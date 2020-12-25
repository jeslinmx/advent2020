# Problem: https://adventofcode.com/2020/day/25

# Input
from sys import stdin
pk_c, pk_d = list(map(int, stdin))
# pk_c, pk_d = 5764801, 17807724

# Part 1
# hopefully brute force works?
from itertools import count
val = 1
for i in count(1):
    if (val := (val * 7) % 20201227) == pk_c:
        key = pow(pk_d, i, 20201227)
        break
print(key)

# Part 2
print()