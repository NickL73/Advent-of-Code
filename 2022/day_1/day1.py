#!/bin/bash/python3
import re
import sys

def day1(input_file):
    with open(input_file, 'r') as in_file:
        data = in_file.read()
        elves = [sum(int(a) for a in elf.split('\n')) for elf in data.split('\n\n')]

    return max(elves), sum(sorted(elves)[-3:])

if __name__=="__main__":
    p1, p2 = day1(sys.argv[1])
    print(f"Part 1: {p1} --- Part 2: {p2}")