# Problem: https://adventofcode.com/2020/day/?

# Input
from sys import stdin
adapters = sorted([int(line) for line in stdin])

# Part 1
differences = [0, 0, 0, 0]
for cur, prev in zip(adapters, [0] + adapters):
    differences[cur - prev] += 1
differences[3] += 1 # since the device has a joltage 3 greater than the largest
print(differences[1] * differences[3])

# Part 2
# dynamic programming time!
# top-down - i like using __missing__, but this is probably slower than linear
# due to the "in" in the generator
class AdapterArrangements(dict):
    def __init__(self, adapters, *args, **kwargs):
        self.adapters = [0] + adapters # 0 is a "permitted" joltage
        super().__init__()
        self[0] = 1 # there is 1 way of achieving 0 joltage


    def __missing__(self, key):
        self[key] = sum((
            self[joltage]
            for joltage in range(key - 3, key)
            if joltage in self.adapters
        ))
        return self[key]

print(AdapterArrangements(adapters)[max(adapters) + 3])

# bottom-down - linear in number of adapters
arrangements = [1] + [0] * (max(adapters) + 3)
for adapter in adapters + [max(adapters) + 3]:
    arrangements[adapter] = sum(arrangements[max(0, adapter - 3):adapter])
print(arrangements[-1])