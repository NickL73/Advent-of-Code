#!/bin/bash/python3
import sys

def predict_first(sequence):
    if all(x == 0 for x in sequence):
        return 0
    
    else:
        new_sequence = []
        for s in range(0, len(sequence) - 1):
            new_sequence.append(sequence[s+1] - sequence[s])

        pred = sequence[0] - predict_first(new_sequence)
        return pred

def predict_next(sequence, cur_difference):
    if all(x == 0 for x in sequence):
        return 0
    
    else:
        new_sequence = []
        for s in range(0, len(sequence) - 1):
            new_sequence.append(sequence[s + 1] - sequence[s])
        
        pred = cur_difference + predict_next(new_sequence, new_sequence[-1])
        
        return pred

def part2(sequences):
    total = 0
    for s in sequences:
        pred = predict_first(s)
        total += pred

    return total

def part1(sequences):
    total = 0
    for s in sequences:
        pred = s[-1] + predict_next(s, 0)
        total += pred

    return total


def day9(filename, part_2=False):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    sequences = [[int(x) for x in line.strip().split(" ")] for line in lines]

    if not part_2:
        ans = part1(sequences)

    else:
        ans = part2(sequences)

    return ans


if __name__=="__main__":
    ans = day9(sys.argv[1])
    print(f"The answer for part 1 is {ans}.")

    ans = day9(sys.argv[1], True)
    print(f"The answer for part 2 is {ans}.")