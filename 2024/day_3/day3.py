#!/bin/bash/python3
import sys
import re
import math

def day3(input_file):
    part1 = 0
    part2 = 0
    with open(input_file, 'r') as in_file:
        text = in_file.read()

    enabled = True
    matches = re.finditer(r"do(?!n't)|don't|mul\(\d{1,3},\d{1,3}\)", text)
    for substr in matches:
            pre = substr.group()
            if re.match(r"^mul", pre):
                 value = math.prod([int(num) for num in re.findall(r'\d{1,3}', pre)])
                 part1 += value
                 part2 += value if enabled else 0
            elif "do" == pre:
                 enabled = True
            else:
                 enabled = False

    print(f"Part 1: {part1} --- Part 2: {part2}")

if __name__=="__main__":
    day3(sys.argv[1])