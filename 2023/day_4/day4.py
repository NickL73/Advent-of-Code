#!/bin/bash/python3
import re

def recurse_card(cards, card_num):
    count = 1

    scratchoff = cards[card_num].strip().split(":")[1].split("|")
    winning_nums = [int(num) for num in re.findall("\d+", scratchoff[0])]
    my_nums = [int(num) for num in re.findall("\d+", scratchoff[1])]
    matches = len(set(winning_nums).intersection(my_nums))
    
    if matches == 0:
        return count
    
    else:
        for i in range(card_num + 1, card_num + matches + 1):
            count += recurse_card(cards, i)
        
    return count

def day4_p2(filename):
    total = 0

    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            total += recurse_card(lines, i)

    return total

def day4(filename):
    total = 0

    with open(filename, "r") as f:
        for line in f:
            scratchoff = line.split(":")[1].split("|")
            winning_nums = [int(num) for num in re.findall("\d+", scratchoff[0])]
            my_nums = [int(num) for num in re.findall("\d+", scratchoff[1])]

            shared = len(set(winning_nums).intersection(my_nums))
            
            if shared > 0:
                total += 2**(shared - 1)


    return total

if __name__=="__main__":
    total = day4("input.txt")
    print(f"The total for Part 1 is {total}.")

    total = day4_p2("input.txt")
    print(f"The total for Part 2 is {total}.")