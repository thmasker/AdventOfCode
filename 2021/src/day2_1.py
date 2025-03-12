horizont = 0
depth = 0

with open("../input/day2.txt") as file:
    while line := file.readline().rstrip():
        instruction, size = line.split()[0], int(line.split()[1])
        if instruction == "forward":
            horizont += size
        if instruction == "up":
            depth -= size
        if instruction == "down":
            depth += size

print(horizont * depth)
