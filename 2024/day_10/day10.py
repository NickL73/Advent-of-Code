#!/bin/bash/python3
import sys

def rating_dfs(grid, cur_r, cur_c, memo_table):
    rows, cols = len(grid), len(grid[0])

    if (cur_r, cur_c) in memo_table:
        return memo_table[(cur_r, cur_c)]
    
    num_paths = 0
    for move_r, move_c in [(1,0), (0,1), (-1,0), (0,-1)]:
        new_r, new_c = cur_r + move_r, cur_c + move_c
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == grid[cur_r][cur_c] + 1:
            num_paths += rating_dfs(grid, new_r, new_c, memo_table)

    num_paths = 1 if num_paths == 0 and grid[cur_r][cur_c] == 9 else num_paths
    memo_table[(cur_r, cur_c)] = num_paths
    return num_paths


def score_dfs(grid, cur_r, cur_c, visited, reachable):
    rows, cols = len(grid), len(grid[0])

    # Base case
    if grid[cur_r][cur_c] == 9:
        reachable.add((cur_r, cur_c))

    visited.add((cur_r, cur_c))

    for move_r, move_c in [(1,0), (0,1), (-1,0), (0,-1)]:
        new_r, new_c = cur_r + move_r, cur_c + move_c
        if 0 <= new_r < rows and 0 <= new_c < cols:
            if (new_r, new_c) not in visited and grid[new_r][new_c] == grid[cur_r][cur_c] + 1:
                score_dfs(grid, new_r, new_c, visited, reachable)

def day10(input_file):
    with open(input_file, 'r') as in_file:
        grid = [[int(a) for a in line.strip()] for line in in_file.readlines()]

    trailheads = [(row_idx, col_idx) for row_idx, row in enumerate(grid) for col_idx, value in enumerate(row) if value == 0]

    p1 = 0
    p2 = 0
    for row, col in trailheads:
        visited = set()
        reachable = set()

        score_dfs(grid, row, col, visited, reachable)
        p1 += len(reachable)
        p2 += rating_dfs(grid, row, col, dict())

    return p1, p2

if __name__=="__main__":
    p1, p2 = day10(sys.argv[1])
    print(f"Part 1: {p1} --- Part 2: {p2}")