#!/bin/bash/python3
import sys

def day15(filename):
    inputs = []
    with open(filename, "r") as file:
        for line in file:
            inputs.extend(line.strip().split(","))

    values = []
    for i in inputs:
        hash = 0
        for c in i:
            hash += ord(c)
            hash *= 17
            hash = (hash % 256)
        
        values.append(hash)

    return sum(values)
        

if __name__=="__main__":
    p1 = day15(sys.argv[1])
    print(f"The answer for Part 1 is {p1}.")