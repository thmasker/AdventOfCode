def get_register() -> list[int]:
    instructions = []
    for instruction in [line.rstrip() for line in open('input.txt').readlines()]:
        instructions.append(0)
        if instruction[:4] == 'addx':
            instructions.append(int(instruction[5:]))

    register = [1 for _ in range(len(instructions) + 1)]
    for i in range(1, len(register)):
        register[i] = register[i - 1] + instructions[i - 1]
    return register


def part1() -> int:
    register = get_register()
    return sum([register[i] * i for i in range(20, 221, 40)])


def part2() -> list[list[str]]:
    register = get_register()
    grid = [['.' for _ in range(40)] for _ in range(6)]
    for cycle in range(240):
        row, column = cycle // 40, cycle % 40
        if column - 1 <= register[cycle] <= column + 1:
            grid[row][column] = '#'
    return grid


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print('Part 2:')
    [print(''.join(row)) for row in part2()]
