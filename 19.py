# Problem: https://adventofcode.com/2020/day/19

# Input
from sys import stdin
rules, msgs = "".join(stdin).split("\n\n")
rules = dict(line.split(": ") for line in rules.split("\n"))
msgs = msgs.split("\n")

# Part 1
import re
regexps = {}
def rule_to_regexp(number):
    if number not in regexps:
        if '"' in rules[number]:
            regexps[number] = rules[number][1:-1]
        else:
            regexps[number] = "|".join((
                "".join((
                    rule_to_regexp(number)
                    for number in subrule.split()
                ))
                for subrule in rules[number].split(" | ")
            ))
            # if there are subrules, encapsulate in group
            if "|" in rules[number]:
                regexps[number] = f"(?:{regexps[number]})"
    return regexps[number]

print(len(list(filter(lambda x: re.fullmatch(rule_to_regexp("0"), x), msgs))))

# Part 2
regexps = {}
# "(Remember, you only need to handle the rules you have; building a solution
# that could handle any hypothetical combination of rules would be
# significantly more difficult.)"
# 8: 42 | 42 8 i.e. 8: 42+
regexps["8"] = f"(?:{rule_to_regexp('42')})+"
# 11: 42 31 | 42 11 31 i.e. 8: 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | etc...
regexps["11"] = f"(?:(?:{rule_to_regexp('42')})(?:{rule_to_regexp('31')})|(?:{rule_to_regexp('42')}){{2}}(?:{rule_to_regexp('31')}){{2}}|(?:{rule_to_regexp('42')}){{3}}(?:{rule_to_regexp('31')}){{3}}|(?:{rule_to_regexp('42')}){{4}}(?:{rule_to_regexp('31')}){{4}})" # blursed regex

print(len(list(filter(lambda x: re.fullmatch(rule_to_regexp("0"), x), msgs))))