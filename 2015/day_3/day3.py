import sys

def day3(filename):
    with open(filename, "r") as file:
        directions = file.readline().strip()
    
    total_visited = set()
    santa_visited = set()
    robo_visited = set()

    current_pos = (0, 0)
    santa_pos = (0, 0)
    robo_pos = (0, 0)

    total_visited.add(current_pos)
    santa_visited.add(santa_pos)
    robo_visited.add(robo_pos)

    index = 0
    for move in directions:
        change_pos = santa_pos if index % 2 == 0 else robo_pos

        if move == "^":
            current_pos = (current_pos[0], current_pos[1] + 1)
            change_pos = (change_pos[0], change_pos[1] + 1)
        
        elif move == "v":
            current_pos = (current_pos[0], current_pos[1] - 1)
            change_pos = (change_pos[0], change_pos[1] - 1)
        
        elif move == ">":
            current_pos = (current_pos[0] + 1, current_pos[1])
            change_pos = (change_pos[0] + 1, change_pos[1])
        
        elif move == "<":
            current_pos = (current_pos[0] - 1, current_pos[1])
            change_pos = (change_pos[0] - 1, change_pos[1])

        if index % 2 == 0:
            santa_pos = change_pos
        
        else:
            robo_pos = change_pos

        index += 1
    
        total_visited.add(current_pos)
        santa_visited.add(santa_pos)
        robo_visited.add(robo_pos)
    
    print(f"The answer for Part 1 is {len(total_visited)}.") 
    print(f"The answer for Part 2 is {len(santa_visited.union(robo_visited))}.")  


if __name__ == "__main__":
    day3(sys.argv[1])