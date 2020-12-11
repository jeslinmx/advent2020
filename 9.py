# Problem: https://adventofcode.com/2020/day/9

# Input
from sys import stdin
n = [int(line) for line in stdin]
k = 25

# Part 1
from bisect import bisect_left
# rolling 2sum has a time complexity of O(nk)
preamble = sorted(n[:k]) # initial sort is O(k log k)
for i, x in enumerate(n[k:]): # O(n)
    # reusing the meet in the middle method from day 1, which is O(k)
    left, right = 0, k - 1
    while left != right:
        balance = x - preamble[left] - preamble[right]
        if balance == 0: # 2sum found, this is not the encoding error
            break
        elif balance > 0:
            left += 1
        else:
            right -= 1
    if left == right: # search completed without finding valid sum
        break

    # replacing the already-sorted preamble with a new slice incurs O(k log k)
    # for the sort, so we remove the outgoing element and insert the incoming
    # element for 2 * O(k) + O(log k) = O(k)
    preamble.insert(bisect_left(preamble, x, lo=right), x)
    preamble.remove(n[i])

print(x)

# Part 2
from itertools import accumulate
cumsum = list(accumulate(n)) + [0] # so that cumsum[0 - 1] = 0
for i in range(0, len(n)):
    for j in range(i + 1, len(n)):
        if x == cumsum[j] - cumsum[i - 1]:
            print(min(n[i:j+1]) + max(n[i:j+1]))