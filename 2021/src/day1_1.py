increased_measures = 0

with open("../input/day1.txt") as file:
    first = int(file.readline().rstrip())
    while line := file.readline().rstrip():
        second = int(line)
        if second > first:
            increased_measures += 1
        first = second

print(increased_measures)
