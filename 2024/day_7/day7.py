#!/bin/bash/python3
import re
import sys


def validate_operations(target, current, rest, concat=False):
    if len(rest) == 0:
        return target == current
    
    elif current > target:
        return False

    if validate_operations(target, current + rest[0], rest[1:], concat):
        return True
    
    if validate_operations(target, current * rest[0], rest[1:], concat):
        return True
    
    if concat and validate_operations(target, int(f"{current}{rest[0]}"), rest[1:], concat):
        return True

    return False

def day7(input_file):
    with open(input_file, 'r') as in_file:
        probs = [(int(target), list(map(int, numbers.split()))) 
                 for line in in_file.read().splitlines() 
                 for target, numbers in [re.match(r"(\d+):\s+(.*)", line).groups()]
        ]
    
    p1 = sum(tar for tar, nums in probs if validate_operations(tar, nums[0], nums[1:]))
    p2 = sum(tar for tar, nums in probs if validate_operations(tar, nums[0], nums[1:], True))
    return p1, p2

if __name__=="__main__":
    p1, p2 = day7(sys.argv[1])
    print(f"Part 1: {p1} --- Part 2: {p2}")