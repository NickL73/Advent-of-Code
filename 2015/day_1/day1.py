import sys

def day1(filename):

    with open(filename, "r") as file:
        line = file.readline().strip()

    count = 0
    found = False
    for i in range(len(line)):
        if line[i] == "(":
            count += 1
        else:
            count -= 1

        if count < 0 and not found:
            found = True
            print(f"First basement position is {i + 1}.")
    
    print(f"Total floors is {count}.")

if __name__ == "__main__":
    day1(sys.argv[1])