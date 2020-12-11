# Problem: https://adventofcode.com/2020/day/4

# Input
from sys import stdin
passports = [
    dict([
        field.split(":")
        for field in passport.replace("\n", " ").split()
    ])
    for passport in "".join(stdin).split("\n\n")
]

# Part 1
expectedfields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
print(sum((
    1 for passport in passports
    if expectedfields <= set(passport.keys())
)))

# Part 2
import re
print(sum((
    1 for passport in passports 
    if (
        expectedfields <= set(passport.keys())
        and len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002
        and len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020
        and len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030
        and (
            (passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193)
            or (passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76)
        )
        and re.fullmatch(r"#[0-9a-f]{6}", passport["hcl"])
        and passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        and re.fullmatch(r"\d{9}", passport["pid"])
    )
)))