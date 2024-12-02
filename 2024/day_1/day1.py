#!/bin/bash/python3
import re
import sys
import collections

def day1(input_file):
    part_1 = 0
    part_2 = 0

    with open(input_file, "r") as in_file:
        text = ' '.join(in_file.read().splitlines())
    
    locations = [int(converted) for converted in re.split(r'\s+', text)]
    
    first_elf = sorted(locations[::2])
    second_elf = sorted(locations[1::2])
    frequency = collections.Counter(second_elf)

    # Part 1
    for i in range(len(first_elf)):
        part_1 += abs(first_elf[i] - second_elf[i])
        part_2 += (first_elf[i] * frequency[first_elf[i]])

    print(f"Part 1: {part_1} --- Part 2: {part_2}")

if __name__ == "__main__":
    day1(sys.argv[1])
