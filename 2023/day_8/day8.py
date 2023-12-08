#!/bin/bash/python3
import sys
import re
import numpy as np

def part_2(directions, mapping):
    starting_points = []
    end_points = []
    for waypoint in mapping.keys():
        if waypoint[2] == 'A':
            starting_points.append(waypoint)
        
        if waypoint[2] == 'Z':
            end_points.append(waypoint)

    steps_per_node = []
    for node in starting_points:
        cur_pos = node
        steps = 0
        cur_index = 0

        while cur_pos not in end_points:
            next_step = 0 if directions[cur_index] == 'L' else 1

            cur_pos = mapping[cur_pos][next_step]
            steps += 1
            
            if cur_index == len(directions) - 1:
                cur_index = 0
            
            else:
                cur_index += 1

        steps_per_node.append(steps)
    
    return np.lcm.reduce(steps_per_node)


def part_1(directions, mapping):
    steps = 0

    cur_pos = "AAA"
    cur_index = 0
    while cur_pos != "ZZZ":
        next_step = 0 if directions[cur_index] == 'L' else 1

        cur_pos = mapping[cur_pos][next_step]
        steps += 1
        
        if cur_index == len(directions) - 1:
            cur_index = 0
        
        else:
            cur_index += 1

    return steps

def day8(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    directions = lines[0].strip()
    mapping = dict()

    for i in range(1, len(lines)):
        if lines[i] == "\n":
            continue

        elements = re.findall("[a-zA-z]+", lines[i])
        mapping[elements[0]] = (elements[1], elements[2])

    steps = part_1(directions, mapping)
    print(f"The answer to Part 1 is {steps} steps.")

    steps = part_2(directions, mapping)
    print(f"The answer to Part 2 is {steps} steps.")
    
if __name__=="__main__":
    day8(sys.argv[1])
    