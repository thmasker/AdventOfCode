horizont = 0
depth = 0
aim = 0

with open("../input/day2.txt") as file:
    while line := file.readline().rstrip():
        instruction, size = line.split()[0], int(line.split()[1])
        if instruction == "forward":
            horizont += size
            depth += aim * size
        if instruction == "up":
            aim -= size
        if instruction == "down":
            aim += size

print(horizont * depth)
