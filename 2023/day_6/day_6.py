#!/bin/bash/python3
import sys
import re
import math

def parse_input(filename):
    with open(filename, "r") as in_f:
        lines = in_f.readlines()
    
    times = [int(t) for t in re.findall("\d+", lines[0])]
    distances = [int(d) for d in re.findall("\d+", lines[1])]

    return [(times[i], distances[i]) for i in range(0, len(times))]

def day6(filename, part2=False):
    races = parse_input(filename)

    winning_vals = []
    p2_time = ""
    p2_dist = ""
    for race in races:
        p2_time += str(race[0])
        p2_dist += str(race[1])

        ways_to_win = 0
        for time in range(0, race[0] + 1):
            dist = (race[0] - time) * time
            if dist > race[1]:
                ways_to_win += 1
        
        winning_vals.append(ways_to_win)
    
    part1 = math.prod(winning_vals)

    part2 = 0
    for time in range(0, int(p2_time) + 1):
        dist = (int(p2_time) - time) * time
        if dist > int(p2_dist):
            part2 += 1

    return part1, part2

if __name__=="__main__":
    part1, part2 = day6(sys.argv[1])
    print(f"The value for day 6 part 1 is {part1}.")
    print(f"The value for day 6 part 2 is {part2}.")
