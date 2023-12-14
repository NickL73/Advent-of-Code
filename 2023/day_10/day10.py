#!/bin/bash/python3
import sys

valid_directional_moves = {
    "N": ["|", "7", "F"],
    "S": ["|", "L", "J"],
    "E": ["-", "J", "7"],
    "W": ["-", "F", "L"]
}

moves = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)]
}

def scan_for_s(lines):
    line_idx = 0
    for line in lines:
        pos_idx = 0
        for spot in line:

            if spot == "S":
                return (line_idx, pos_idx)
            
            pos_idx += 1
        line_idx += 1
    
    return (None, None)

def move(lines, cur_pos, last_pos):
    cur_pipe = lines[cur_pos[0]][cur_pos[1]]

    valid_moves = moves[cur_pipe]
    possible_moves = []
    for i in range(len(valid_moves)):
        possible_moves.append(tuple(map(sum, zip(valid_moves[i], cur_pos))))
    
    next_pos = possible_moves[1 - possible_moves.index(last_pos)]
    return next_pos

def move_off_start(lines, starting_pos):
    line_num = starting_pos[0]
    pos_idx = starting_pos[1]

    if lines[line_num - 1][pos_idx] in "|F7":
        line_num -= 1

    elif lines[line_num + 1][pos_idx] in "|JL":
        line_num += 1

    elif lines[line_num][pos_idx - 1] in "-LF":
        pos_idx -= 1
    
    elif lines[line_num][pos_idx + 1] in "-J7":
        pos_idx += 1

    return (line_num, pos_idx)

def part_1(lines, starting_pos):
    count = 0

    prev_pos = starting_pos
    cur_pos = move_off_start(lines, starting_pos)
    count += 1

    while lines[cur_pos[0]][cur_pos[1]] != "S":
        next_pos = move(lines, cur_pos, prev_pos)

        prev_pos = cur_pos
        cur_pos = next_pos
        count += 1

    return int(count/2)   


def day10(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    starting_pos = scan_for_s(lines)

    return part_1(lines, starting_pos)

        

if __name__=="__main__":
    p1 = day10(sys.argv[1])
    print(f"The answer for Part 1 is {p1}.")
    #print(f"The answer for Part 2 is {p2}.")