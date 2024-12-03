#!/bin/bash/python3
import sys
import re
import math

def day3(input_file):
    part1 = 0
    part2 = 0
    with open(input_file, 'r') as in_file:
        text = in_file.read()
    
    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)
    for match in matches:
        part1 += math.prod([int(num) for num in re.findall(r'\d{1,3}', match)])

    print(f"Part 1: {part1} --- Part 2: {part2}")

if __name__=="__main__":
    day3(sys.argv[1])