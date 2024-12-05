#!/bin/bash/python3
import re
import sys
from collections import defaultdict, deque

# Khan's algorithm
def sort_and_middle(pages, rules_graph):
    indeg = {page: 0 for page in pages}
    for page in pages:
        for after in rules_graph[page]:
            if after in indeg:
                indeg[after] += 1
    
    queue = deque([page for page in pages if indeg[page] == 0])
    sorted_pages = []
    
    while queue:
        page = queue.popleft()
        sorted_pages.append(page)
        for neighbor in rules_graph[page]:
            if neighbor in indeg:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
    
    return sorted_pages[len(sorted_pages)//2]

def day5(input_file):
    with open(input_file, "r") as in_file:
        data = in_file.read()
    
    pairs = [(int(a), int(b)) for a, b in (x.split("|") for x in re.findall(r'\d+[\|]\d+', data))]
    to_validate = [[int(n) for n in line.split(',')] for line in data.strip().split('\n') if re.match(r"^\d+(?:,\d+)*$", line)]

    visit_after = defaultdict(set)
    for before, after in pairs:
        visit_after[before].add(after)

    part1 = 0
    part2 = 0
    for pages in to_validate:
        visited = set()
        for idx in range(len(pages)):
            visited.add(pages[idx])
            if len(visit_after[pages[idx]].intersection(visited)):
                part2 += sort_and_middle(pages, visit_after)
                break
        else:
            part1 += pages[len(pages)//2]
    
    
    
    print(f"Part 1: {part1} --- Part 2: {part2}")

if __name__=="__main__":
    day5(sys.argv[1])