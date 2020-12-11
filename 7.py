# Problem: https://adventofcode.com/2020/day/7

# Input
from sys import stdin
from collections import defaultdict
# at last! a worthy opponent! our battle will be legendary!
# processing the input into a weighted directed (acyclic?) graph
# vertices represent bag types
# an edge of weight n from A to B means bag A can hold n of bag B
adj = defaultdict(dict)
for rule in stdin:
    if "no other" in rule:
        # we don't need to process nodes with no outgoing edges
        # the defaultdict handles that
        continue
    A, Bs = rule.split(" bags contain ")
    for substr in Bs.split(", "):
        weight, B = substr.split(" ", maxsplit=1)
        weight = int(weight)
        B = B.split(" bag", maxsplit=1)[0]
        adj[A][B] = weight

# Part 1
# DFS starting from "shiny gold" and count how many nodes we hit
visited = defaultdict(bool)
def visit(bag):
    for node in filter(lambda key: bag in adj[key], adj):
        if not visited[node]:
            visited[node] = True
            visit(node)

visit("shiny gold")
print(len(visited))

# Part 2
# Create an overlaying graph where the value of each vertex is the weighted sum
# of its neighbours (the number of bags each contains, times the number of bags
# the outer bag holds) plus 1 (the outer bag itself)
class BagsContained(dict):
    def __missing__(self, key):
        self[key] = sum((weight * self[node] for node, weight in adj[key].items())) + 1
        return self[key]

# BagsContained returns a count which includes the bag itself
print(BagsContained()["shiny gold"] - 1)