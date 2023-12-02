#!/bin/bash/python3
import re

def calculate_power(game):
    mins = {
        "r": 0,
        "g": 0,
        "b": 0
    }

    stripped = game.partition(": ")[2]

    draws = re.split('; |, ', stripped)
    for draw in draws:
        sep = draw.split(" ")

        num_shown = int(sep[0])
        
        if num_shown > mins[sep[1][0]]:
            mins[sep[1][0]] = num_shown
    
    game_power = 1
    for i in mins:
        game_power *= mins[i]
    
    return game_power


def check_game(game):
    valid = {
        "r": 12,
        "g": 13,
        "b": 14
    }
    stripped = game.partition(": ")[2]

    draws = re.split('; |, ', stripped)
    for draw in draws:
        sep = draw.split(" ")

        num_shown = int(sep[0])
        
        if num_shown > valid[sep[1][0]]:
            return False
    
    return True

def day2(file, part):
    total = 0

    with open(file, "r") as f:
        if part == 1:
            game_num = 1
            for line in f:
                if check_game(line):
                    total += game_num
                game_num += 1
        
        else:
            for line in f:
                total += calculate_power(line)
    
    return total

if __name__ == "__main__":
    val = day2("day2.txt", 1)
    print(f"The answer for Day 2, Part 1 is {val}.")

    val = day2("day2.txt", 2)
    print(f"The answer for Day 2, Part 2 is {val}.")