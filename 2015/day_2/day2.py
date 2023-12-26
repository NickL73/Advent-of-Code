import sys
from itertools import combinations
from math import prod

def day2(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    ribbon = 0
    wrapping_paper = 0
    for line in lines:
        nums = [int(x) for x in line.strip().split("x")]
        combos = list(combinations(nums, 2))

        volume = prod(nums)
        smallest_permim = None
        smallest_area = None

        for combo in combos:
            area = (combo[0] * combo[1])
            perim = 2*combo[0] + 2*combo[1]

            if not smallest_area or area < smallest_area:
                smallest_area = area
            
            if not smallest_permim or perim < smallest_permim:
                smallest_permim = perim
            
            wrapping_paper += 2 * area
        
        ribbon += volume + smallest_permim
        wrapping_paper += smallest_area
    
    print(f"The elves need {wrapping_paper} square feet of wrapping paper.")
    print(f"The elves need {ribbon} feet of ribbon.")


if __name__ == "__main__":
    day2(sys.argv[1])