# Problem: https://adventofcode.com/2020/day/5

# Input
from sys import stdin
# wait, is this just binary?
ids = [
    int(string.strip()
        .replace("F", "0").replace("B", "1")
        .replace("L", "0").replace("R", "1"), base=2) 
    for string in stdin
]

# Part 1
print(max(ids))

# Part 2
print(int(
    # the expected sum of all the integers between min and max is the max-th triangle number minus the (min-1)th triangle number
    (0.5 * max(ids) * (max(ids) + 1)) - (0.5 * (min(ids) - 1) * min(ids))
    # the missing number is the difference between the expected sum and the actual sum
    - sum(ids)
))