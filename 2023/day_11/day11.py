#!/bin/bash/python3
import sys


def prep_grid(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    expanded = []
    for line in lines:
        line = list(line.strip())
        if all(x == "." for x in line):
            expanded.append(line)
        expanded.append(line)
    
    rotated = [[x[i] for x in expanded] for i in range(len(expanded[0]))]
    expanded = []
    for line in rotated:
        if all(x == "." for x in line):
            expanded.append(line)
        expanded.append(line)
    
    return expanded

def find_points(grid):
    coords = []
    
    line_num = 0
    for line in grid:
        matches = [i for i, x in enumerate(line) if x == "#"]

        coords.extend((line_num, i) for i in matches)
        line_num += 1
    
    return coords


def day11(filename):
    grid = prep_grid(filename)
    points = find_points(grid)

    total = 0
    for i in range(len(points)):
        for j in range(i, len(points)):
            disty = abs(points[i][0] - points[j][0])
            distx = abs(points[i][1] - points[j][1])

            total += (disty + distx)
    
    return total
        

if __name__=="__main__":
    p1 = day11(sys.argv[1])
    print(f"The answer for Part 1 is {p1}.")
