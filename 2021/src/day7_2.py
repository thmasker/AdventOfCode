def cost(steps):
    return int(steps * (steps + 1) / 2)


def main():
    with open("../input/day7.txt") as file:
        initial_positions = list(map(int, file.readline().split(',')))

    best_pos = 0
    fuel = max(initial_positions)**3
    for final_position in range(max(initial_positions) + 1):
        current_fuel = 0
        for initial_position in initial_positions:
            current_fuel += cost(abs(initial_position - final_position))

        if current_fuel < fuel:
            fuel = current_fuel
            best_pos = final_position

    print(f'Optimal position: {best_pos}')
    print(f'Fuel spent: {fuel}')


if __name__ == '__main__':
    main()
