from src.Lanternfish import Lanternfish


days = 80
lanternfish = []

with open("../input/day6.txt") as file:
    line = file.readline()[:-1].split(',')

    for n in line:
        lanternfish.append(Lanternfish(int(n)))

    # print(f"Initial state: {[fish.timer for fish in lanternfish]}")

    for day in range(days):
        for i in range(len(lanternfish)):
            new_fish = lanternfish[i].update()

            if new_fish:
                lanternfish.append(new_fish)

        # print(f"Day {day + 1}: {[fish.timer for fish in lanternfish]}")

    print(len(lanternfish))
