#!/bin/bash/python3

def get_digit(line):
    dig1 = 0
    dig2 = 0

    for c in line:
        if c.isdigit():
            dig1 = int(c)
            break
    
    for c in reversed(line):
        if c.isdigit():
            dig2 = int(c)
            break
    
    total = (10 * dig1) + dig2
    return total

def convert_strings(line):
    nums = {"one": "o1e", 
            "two": "t2o", 
            "three": "th3ee", 
            "four": "fo4r", 
            "five": "fi5e", 
            "six": "s6x", 
            "seven": "se7en", 
            "eight": "ei8ht", 
            "nine": "ni9e"}

    new_line = line
    for key in nums.keys():
        new_line = new_line.replace(key, nums[key])

    return new_line

def day1(file, p2=False):
    total = 0

    with open(file, "r") as in_file:
        for line in in_file:
            
            if p2:
                line = convert_strings(line)

            digits = get_digit(line)
            total += digits

    return total

if __name__=="__main__":
    total = day1("day1.txt")
    print(f"Part 1: {total}")

    total = day1("day1.txt", True)
    print(f"Part 2: {total}")