# Problem: https://adventofcode.com/2020/day/18

# Input
from sys import stdin
expressions = [line.strip() for line in stdin]

# Part 1
from collections import deque
from operator import add, mul
def p1evaluate(expression):
    ctx = deque([{}])
    tokens = deque(
        expression
        .replace("(", "( ")
        .replace(")", " )")
        .split()
    )
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == "+":
            ctx[-1]["operator"] = add
        elif token == "*":
            ctx[-1]["operator"] = mul
        elif token == "(":
            # add nest level in ctx
            ctx.append({})
        elif token == ")":
            # pop nest level and push its value onto stack
            tokens.appendleft(ctx.pop()["value"])
        else:
            ctx[-1]["value"] = ctx[-1]["operator"](ctx[-1]["value"], int(token))if "value" in ctx[-1] else int(token)
    return ctx[-1]["value"]

print(sum(map(p1evaluate, expressions)))

# Part 2
from math import prod
def p2evaluate(expression):
    if isinstance(expression, str):
        tokens = deque(
            expression
            .replace("(", "( ")
            .replace(")", " )")
            .split()
        )
    else:
        tokens = expression
    # resolve all brackets
    tokens_no_brackets = deque()
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == "(":
            # use recursion to evaluate to the closing bracket
            result, tokens = p2evaluate(tokens)
            tokens.appendleft(result)
        elif token == ")":
            # stop evaluation at this point; remaining tokens become remnant
            remnant = tokens
            break
        else:
            tokens_no_brackets.append(token)
    # resolve addition
    tokens = tokens_no_brackets
    tokens_addition_done = deque()
    while len(tokens) > 0:
        token = tokens.popleft()
        if token == "+":
            # pop off last transferred value, pop off next value, add them
            # together, then put it back
            tokens_addition_done.append(
                int(tokens_addition_done.pop()) + int(tokens.popleft())
            )
        else:
            tokens_addition_done.append(token)
    # resolve multiplication
    result = prod(map(int, filter(lambda x: x != "*", tokens_addition_done)))
    try:
        return result, remnant
    except UnboundLocalError:
        # if remnant is undefined, that's because this is the outermost call
        # (and hence no closing bracket was ever seen)
        return result

print(sum(map(p2evaluate, expressions)))