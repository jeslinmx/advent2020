# Problem: https://adventofcode.com/2020/day/2

# Input
from sys import stdin
import re
db = [
    re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    for line in stdin
]

# Part 1
print(sum((
    1 for lower, upper, char, password in db
    if int(lower) <= password.count(char) <= int(upper)
)))

# Part 2
print(sum((
    1 for lower, upper, char, password in db
    if (password[int(lower)-1] == char) ^ (password[int(upper)-1] == char)
)))