#!/bin/bash/python3
import sys
from itertools import product


def day4(input_file):
    part1 = 0
    part2 = 0

    with open(input_file, "r") as in_file:
        arr = [list(line.strip()) for line in in_file.readlines()]
    
    rows, cols = len(arr), len(arr[0])
    directions = list(product([-1, 0, 1], repeat=2))
    
    target = "XMAS"
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            for hor, ver in directions:
                invalid = False
                for i in range(len(target)):
                    r, c = row + i * hor, col + i * ver
                    if not (0 <= r < rows and 0 <= c < cols) or arr[r][c] != target[i]:
                        invalid = True
                part1 += 1 if not invalid else 0
        
            if (0 < row < (len(arr) - 1)) and (0 < col < (len(arr[0]) - 1)):
                if arr[row][col] == 'A':
                    top_right = arr[row - 1][col + 1]
                    bottom_right = arr[row + 1][col + 1]
                    top_left = arr[row - 1][col - 1]
                    bottom_left = arr[row + 1][col - 1]

                    left_x = (top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M')
                    right_x = (top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M')
                    if left_x and right_x:
                        part2 += 1

    print(f"Part 1: {part1} --- Part 2: {part2}")    

if __name__=="__main__":
    day4(sys.argv[1])