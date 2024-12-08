#!/bin/bash/python3
import sys
from itertools import cycle

def simulate_guard(arr, start_pos, add_obstacle = None):
    grid = [row[:] for row in arr]
    if add_obstacle:
        grid[add_obstacle[0]][add_obstacle[1]] = '#'
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    moves = cycle(directions)
    
    history = set()
    visited = set()

    cur_pos = start_pos
    cur_dir = next(moves)
    next_pos = None
    while (0 <= cur_pos[0] < len(grid)) and (0 <= cur_pos[1] < len(grid[0])):
        state = (cur_pos, cur_dir)
        if state in history:
            return None
        
        history.add(state)

        visited.add(cur_pos)
        next_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])

        if (0 <= next_pos[0] < len(grid)) and (0 <= next_pos[1] < len(grid[0])):
            if '#' == grid[next_pos[0]][next_pos[1]]:
                cur_dir = next(moves)
                continue
            cur_pos = next_pos
        
        else:
            break
    
    return visited

def day6(input_file):

    with open(input_file, "r") as in_file:
        grid = [list(line.strip()) for line in in_file.readlines()]

    for row, v in enumerate(grid):
        if '^' in v:
            col_s = v.index('^')
            break
    start_pos = (row, col_s)

    p1_visited = simulate_guard(grid, start_pos)
    
    p2 = 0
    for row, col in p1_visited:
            p2 += 1 if not simulate_guard(grid, start_pos, (row, col)) else 0

    return len(p1_visited), p2

if __name__=="__main__":
    p1, p2 = day6(sys.argv[1])
    print(f"Part 1: {p1} --- Part 2: {p2}")