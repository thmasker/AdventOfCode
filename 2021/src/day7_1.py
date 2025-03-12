def fuel_cost(positions, final_position):
    total_fuel = 0
    for pos in positions:
        total_fuel += abs(pos - final_position)

    return total_fuel


def main():
    with open("../input/day7.txt") as file:
        initial_positions = list(map(int, file.readline().split(',')))

    fuel = fuel_cost(initial_positions, 0)
    best_pos = 0
    for pos in range(1, max(initial_positions)):
        current_cost = fuel_cost(initial_positions, pos)

        if current_cost < fuel:
            fuel = current_cost
            best_pos = pos

    print(f'Optimal position: {best_pos}')
    print(f'Fuel spent: {fuel}')


if __name__ == '__main__':
    main()
