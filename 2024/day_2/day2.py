#!/bin/bash/python3
import sys
import re

def day2(input_file):
    safe = 0
    safe_with_dampener = 0
    
    with open(input_file, 'r') as inp:
        lines = [[int(val) for val in re.split(r'\s+', line.strip())] for line in inp.readlines()]
    
    for line in lines:
        if all(((earlier > later) and (earlier - later <= 3))for earlier, later in zip(line, line[1:])):
            safe += 1

        if all(((earlier < later) and (later - earlier <= 3)) for earlier, later in zip(line, line[1:])):
            safe += 1

    print(f"Part 1: {safe} - Part 2 {safe_with_dampener}")

if __name__ == "__main__":
    day2(sys.argv[1])
