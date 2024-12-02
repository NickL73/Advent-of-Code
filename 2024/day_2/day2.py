#!/bin/bash/python3
import sys
import re

def is_safe(line, ascending):
    if ascending:
        return all((earlier < later and later - earlier <= 3) for earlier, later in zip(line, line[1:]))
    else:
        return all((earlier > later and earlier - later <= 3) for earlier, later in zip(line, line[1:]))


def day2(input_file):
    safe = 0
    safe_with_dampener = 0
    
    with open(input_file, 'r') as inp:
        lines = [[int(val) for val in re.split(r'\s+', line.strip())] for line in inp.readlines()]
    
    for line in lines:
        if is_safe(line, True) or is_safe(line, False):
            safe += 1
            continue

        for i in range(len(line)):
            drop = line[:i] + line[i+1:]
            if is_safe(drop, True) or is_safe(drop, False):
                safe_with_dampener += 1
                break

    print(f"Part 1: {safe} --- Part 2: {safe + safe_with_dampener}")

if __name__ == "__main__":
    day2(sys.argv[1])