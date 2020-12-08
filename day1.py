# Problem: https://adventofcode.com/2020/day/1

# Input
from sys import stdin
report = [int(line.strip()) for line in stdin]

# Part 1
# naive brute force
# o(n^2)
for i, num in enumerate(report):
    for num2 in report[i+1:]:
        if num + num2 == 2020:
            print(num, num2)
            print(num * num2)

# sort and binary search
# o(n log n)
from bisect import bisect_left
resort = sorted(report)
for i, num in enumerate(resort[:-1]): # stop at the 2nd last element, since there are 0 remaining elements at the last element
    target = 2020 - num
    remaining = resort[i+1:]
    target_index = bisect_left(remaining, target) # search to the right of current element for target value
    if remaining[target_index] == target:
        print(num, remaining[target_index])
        print(num * remaining[target_index])

# sort and meet in the middle
# o(n log n) overall, but o(n) for search phase
# sum the smallest item (on the left) with the largest item (on the right)
# if the sum is exactly 2020, that is a match
# if it is too large, we know that we can ignore the right value and anything larger than it in the future
# if it is too small, we know that we can ignore the left value and anything smaller than it in the future
left, right = 0, len(resort) - 1
while left != right:
    balance = 2020 - resort[left] - resort[right]
    if balance == 0: # a match!
        print(resort[left], resort[right])
        print(resort[left] * resort[right])
        left += 1 # we shift both bounds inwards, since we are not treating duplicates specially
        right -= 1
    elif balance > 0: # we need bigger numbers - increasing the left bound
        left += 1
    else: # we need smaller numbers - decreasing the right bound
        right -= 1

# Part 2
# naive brute force
# o(n^3)
for i, num in enumerate(report):
    for j, num2 in enumerate(report[i+1:], start=i+1):
        for num3 in report[j+1:]:
            if num + num2 + num3 == 2020:
                print(num, num2, num3)
                print(num * num2 * num3)

# sort, linear sweep + meet in the middle
# o(n^2)
# remove the leftmost item and use the meet in the middle method from part 1 on the remaining items, looking for 2020 - item
# then remove another leftmost item and repeat
for left, item in enumerate(resort[:-2]):
    middle, right = 0, len(resort[left+1:]) - 1
    while middle != right:
        balance = 2020 - item - resort[left+1:][middle] - resort[left+1:][right]
        guess = bisect_left(resort[left+1:][middle+1:right], balance)
        if balance == 0: # a match!
            print(item, resort[left+1:][middle], resort[left+1:][right])
            print(item * resort[left+1:][middle] * resort[left+1:][right])
            left += 1 # we shift both bounds inwards, since we are not treating duplicates specially
            right -= 1
        elif balance > 0: # we need bigger numbers - increasing the left bound
            left += 1
        else: # we need smaller numbers - decreasing the right bound
            right -= 1