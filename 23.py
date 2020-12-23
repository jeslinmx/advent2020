# Problem: https://adventofcode.com/2020/day/23

# Input
from sys import stdin
initial_cups = list(map(int, stdin.read().strip()))

# Part 1
from collections import deque
class CupsGame(object):
    def __init__(self, initial_cups):
        self.cups = deque(initial_cups)
        self.highest_cup = max(initial_cups)
        self.lowest_cup = min(initial_cups)
    def move(self):
        # the first cup is the current cup, due to rotate
        current = self.cups[0]
        self.cups.rotate(-1)
        # remove 3 cups following current cup
        removed = deque()
        for _ in range(3):
            removed.append(self.cups.popleft())
        # select destination cup
        dest = current
        while True:
            dest -= 1
            if dest < self.lowest_cup:
                dest = self.highest_cup
            if dest not in removed:
                break
        # insert cups clockwise of dest
        removed.reverse()
        for cup in removed:
            self.cups.insert(self.cups.index(dest) + 1, cup)
        return self

part1 = CupsGame(initial_cups)
for _ in range(100):
    part1.move()
# rotate the list until cup 1 is first
part1.cups.rotate(-part1.cups.index(1))
part1.cups.popleft()
print("".join(map(str, part1.cups)))

# Part 2
class CupsGameOptimized(object):
    def __init__(self, initial_cups):
        # leveraging off the fact that the cups are labelled continuously from
        # 1 to n, we can store their arrangement as a linked list within a
        # n-long array, where each index and value are the label of a cup and
        # the label of the cup following it respectively.
        self.cups = [None] * (len(initial_cups) + 1)
        self.highest_cup = len(initial_cups)
        self.lowest_cup = 1
        self.cups[0] = initial_cups[0] # store the current cup at index 0
        for current_cup, next_cup in zip(initial_cups, initial_cups[1:]):
            self.cups[current_cup] = next_cup
        self.cups[next_cup] = self.cups[0] # close the loop
    def move(self):
        # find the first cup we need to remove, which is the cup after current
        head_label = self.cups[self.cups[0]]
        # move 3 cups ahead of head to find the tail, the first unremoved cup
        # at the same time, take note of what we removed
        tail_label = head_label
        removed = deque()
        for _ in range(3):
            removed.append(tail_label)
            tail_label = self.cups[tail_label]
        # connect the current cup to the tail, removing the 3 cups between
        self.cups[self.cups[0]] = tail_label
        # select destination cup
        dest = self.cups[0]
        while True:
            dest -= 1
            if dest < self.lowest_cup:
                dest = self.highest_cup
            if dest not in removed:
                break
        # insert removed cups clockwise of dest
        # connect the last removed cup to the cup after dest
        self.cups[removed[-1]] = self.cups[dest]
        # connect dest to the first removed cup
        self.cups[dest] = head_label
        # advance the current cup
        self.cups[0] = self.cups[self.cups[0]]
    def cups_from(self, label):
        order = ""
        next_cup = label
        for _ in range(len(self.cups) - 2):
            next_cup = self.cups[next_cup]
            order += str(next_cup)
        return order

from itertools import chain
part2 = CupsGameOptimized(list(chain(initial_cups, range(max(initial_cups)+1, 1000001))))
for _ in range(10000000):
    part2.move()
print(part2.cups[1] * part2.cups[part2.cups[1]])