# Problem: https://adventofcode.com/2020/day/8

# Input
from sys import stdin
instructions = [line.split() for line in stdin]

# Part 1
def execute(instructions):
    visited = [False] * len(instructions)
    acc, cur = 0, 0
    while cur < len(instructions) and not visited[cur]:
        visited[cur] = True
        if instructions[cur][0] == "acc":
            acc += int(instructions[cur][1])
            cur += 1
        elif instructions[cur][0] == "jmp":
            cur += int(instructions[cur][1])
        else:
            cur += 1
    return acc, cur >= len(instructions)

print(execute(instructions))

# Part 2
def modify_line(number):
    # return a copy of instructions in which the instruction at
    # the given line number is substituted between jmp and nop
    return (
        instructions[:number]
        + [
            ("jmp" if instructions[number][0] == "nop" else "nop",
            instructions[number][1])
        ]
        + instructions[number+1:]
    )

# brute force through substituting each jmp/nop to find a terminating program
for modified_instructions in (modify_line(number) for number, instruction in enumerate(instructions) if instruction[0] in ("jmp", "nop")):
    result = execute(modified_instructions)
    if result[1]:
        print(result)