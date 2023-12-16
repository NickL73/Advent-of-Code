#!/bin/bash/python3
import sys

def prepare_input(filename, multiplier):
    with open(filename, "r") as file:
        lines = file.readlines()

    grid = []
    for line in lines:
        grid.append((line.strip()))
    
    row_mult = [1 for x in range(len(grid))]
    col_mult = [1 for x in range(len(grid[0]))]

    # Check for empty rows in the grid
    for i in range(len(grid)):
        if all(x == "." for x in grid[i]):
            row_mult[i] = multiplier
    
    # Check for empty columns
    for i in range(len(grid[0])):
        col = ""
        for j in range(len(grid)):
            col += grid[j][i]
        
        if all(x == "." for x in col):
            col_mult[i] = multiplier
    
    return grid, row_mult, col_mult  

def find_points(grid):
    coords = []
    
    line_num = 0
    for line in grid:
        matches = [i for i, x in enumerate(line) if x == "#"]

        coords.extend((line_num, i) for i in matches)
        line_num += 1
    
    return coords


def day11(filename, multiplier):
    grid, row_mult, col_mult = prepare_input(filename, multiplier)
    points = find_points(grid)

    total = 0
    for i in range(len(points)):
        for j in range(i, len(points)):
            min_row, max_row = sorted([points[i][0], points[j][0]])
            min_col, max_col = sorted([points[i][1], points[j][1]])

            dist_col = sum(col_mult[min_col:max_col])
            dist_row = sum(row_mult[min_row:max_row])

            total += dist_col + dist_row

    return total
        

if __name__=="__main__":
    p1 = day11(sys.argv[1], 2)
    print(f"The answer for Part 1 is {p1}.")

    p1 = day11(sys.argv[1], 1000000)
    print(f"The answer for Part 2 is {p1}.")
