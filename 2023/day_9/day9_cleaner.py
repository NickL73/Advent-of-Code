#!/bin/bash/python3
import sys

def get_next_sequence(sequence):
    return([(sequence[s+1] - sequence[s]) for s in range(0, len(sequence) - 1)])


def predict_first(sequence):
    if all(x == 0 for x in sequence):
        return 0
    
    else:
        return(sequence[0] - predict_first(get_next_sequence(sequence)))

def predict_next(sequence):
    if all(x == 0 for x in sequence):
        return 0
    
    else:
        return(sequence[-1] + predict_next(get_next_sequence(sequence)))
    

def day9(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    sequences = [[int(x) for x in line.strip().split(" ")] for line in lines]

    end_total = 0
    beg_total = 0

    for s in sequences:
        end_total += predict_next(s)
        beg_total += predict_first(s)

    return end_total, beg_total


if __name__=="__main__":
    next, first = day9(sys.argv[1])
    print(f"The answer for part 1 is {next}. The answer for part 2 is {first}.")
