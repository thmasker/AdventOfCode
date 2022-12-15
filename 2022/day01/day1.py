def find_n_max_calories(n: int) -> int:
    with open('input.txt', 'r') as file:
        calories = []
        current_calories = 0
        for line in file:
            if line == '\n':
                calories.append(current_calories)
                current_calories = 0
            else:
                current_calories += int(line)

    calories.sort()

    return sum(calories[-n:])


if __name__ == '__main__':
    print(f'Part 1: {find_n_max_calories(1)}')
    print(f'Part 2: {find_n_max_calories(3)}')
