def move(orientation: chr, x: int, y: int, direction: chr, moves: int) -> tuple[int, int, chr]:
    if orientation == 'N' and direction == 'L' or orientation == 'S' and direction == 'R':
        return x - moves, y, 'W'
    if orientation == 'N' and direction == 'R' or orientation == 'S' and direction == 'L':
        return x + moves, y, 'E'
    if orientation == 'E' and direction == 'L' or orientation == 'W' and direction == 'R':
        return x, y + moves, 'N'
    if orientation == 'E' and direction == 'R' or orientation == 'W' and direction == 'L':
        return x, y - moves, 'S'


def part1() -> int:
    x, y = 0, 0
    orientation = 'N'
    instructions = open('input.txt').read().strip().split(', ')
    for instruction in instructions:
        direction = instruction[0]
        moves = int(instruction[1:])
        x, y, orientation = move(orientation, x, y, direction, moves)

    return abs(x) + abs(y)


def part2() -> int:
    x, y = 0, 0
    orientation = 'N'
    visited = set()
    instructions = open('input2.txt').read().strip().split(', ')
    for instruction in instructions:
        direction = instruction[0]
        moves = int(instruction[1:])
        x, y, orientation = move(orientation, x, y, direction, moves)
        if (x, y) in visited:
            return abs(x) + abs(y)
        else:
            visited.add((x, y))


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2  : {part2()}')
