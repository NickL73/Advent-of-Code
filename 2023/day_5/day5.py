#!/bin/bash/python3
import re

def get_conversion(mapping, number):
    converted = number

    for conversions in mapping:
        if conversions[1] <= number < (conversions[1] + conversions[2]):
            converted = conversions[0] + (number - conversions[1])
            break
    
    return converted


def prepare_file(filename, part_2=False):
    conversion_mappings = []

    with open(filename, "r") as file:
        seeds = [int(seed) for seed in re.findall("\d+", file.readline())]
        maps = file.read().split("\n\n")

    if part_2:
        iterable = iter(seeds)
        seeds = [*zip(iterable, iterable)]

    for mapping in maps:
        single_map = []
        for line in mapping.split("\n"):
            nums = [int(x) for x in re.findall("\d+", line)]
            if nums != []:
                single_map.append(nums)
        
        single_map = sorted(single_map, key= lambda x: x[1])
        conversion_mappings.append(single_map)

    return seeds, conversion_mappings

def day5(filename, part2=False):
    lowest = None

    seeds, mappings = prepare_file(filename, part2)
    
    if not part2:
        for seed in seeds:
            cur_num = seed
            for mapping in mappings:
                cur_num = get_conversion(mapping, cur_num)
            
            if not lowest:
                lowest = cur_num

            elif cur_num < lowest:
                lowest = cur_num

    else:
        for seed in seeds:
            for i in range(seed[0], seed[0] + seed[1]):
                cur_num = i
                for mapping in mappings:
                    cur_num = get_conversion(mapping, cur_num)
            
                if not lowest:
                    lowest = cur_num

                elif cur_num < lowest:
                    lowest = cur_num
        

    return lowest


if __name__=="__main__":
    location = day5("input.txt")
    print(f"The answer for part 1 is {location}.")

    lowest = day5("input.txt", True)
    print(f"The answer for part 2 is {lowest}.")