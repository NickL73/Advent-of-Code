#!/bin/bash/python3

def count_middle(line, line_idx):
    num_idx = line_idx

    if line[line_idx] == ".":
        return 0

    while (0 <= num_idx < len(line)) and line[num_idx].isdigit():
        num_idx -= 1
    
    return count_right(line, num_idx)

def count_left(line, start_idx):
    num_left = ""

    num_idx = start_idx - 1
    while(line[num_idx].isdigit()) and (num_idx >= 0):
        num_left = line[num_idx] + num_left
        num_idx -= 1
    
    if num_left == "":
        return 0
    else:
        return int(num_left)

def count_right(line, start_idx):
    num_right = ""
    num_idx = start_idx + 1
    while (num_idx < len(line)) and (line[num_idx].isdigit()):
        num_right += line[num_idx]
        num_idx += 1
    
    if num_right == "":
        return 0
    
    else:
        return int(num_right)
    

def check_part(lines, line_num, line_idx):
    total = 0
    
    # Check left
    total += count_left(lines[line_num], line_idx)
    
    # Check right
    total += count_right(lines[line_num], line_idx)

    # Check top
    if line_num > 0:
        # Check top middle
        top = count_middle(lines[line_num - 1], line_idx)
        
        # Check diagonals
        if top == 0:
            top += count_middle(lines[line_num - 1], line_idx - 1)
            top += count_middle(lines[line_num - 1], line_idx + 1)

        total += top
    
    # Check bottom
    if line_num < len(lines) - 1:
        # Check bottom middle
        bottom = count_middle(lines[line_num + 1], line_idx)
        
        # Check diagonals
        if bottom == 0:
            bottom += count_middle(lines[line_num + 1], line_idx - 1)
            bottom += count_middle(lines[line_num + 1], line_idx + 1)

        total += bottom
    
    return total

def day3(filename):
    total = 0

    with open(filename, "r") as f:
        line_index = 0
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            let_index = 0

            for let in line:
                if let != "." and not let.isdigit():

                    new = check_part(lines, line_index, let_index)
                    total += new
                let_index += 1
            
            line_index += 1

    return total


if __name__=="__main__":
    total = day3("input.txt")
    print(f"The answer for part 1 is {total}.")