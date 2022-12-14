import operator

Position = tuple[int, int]

START_POS = (0, 500)


def get_rocks_coordinates() -> set[Position]:
    rock_paths = open('input.txt').read().split('\n')[:-1]
    rock_positions = set()
    for rock_path in rock_paths:
        positions = rock_path.split(' -> ')
        for position in range(len(positions) - 1):
            start_j, start_i = [int(pos) for pos in positions[position].split(',')]
            end_j, end_i = [int(pos) for pos in positions[position + 1].split(',')]
            if start_i == end_i:
                increment = (end_j - start_j) // abs(end_j - start_j)
                for j in range(start_j, end_j + increment, increment):
                    rock_positions.add((start_i, j))
            else:
                increment = (end_i - start_i) // abs(end_i - start_i)
                for i in range(start_i, end_i + increment, increment):
                    rock_positions.add((i, start_j))
    return rock_positions


ROCKS = get_rocks_coordinates()


def is_allowed_to_go(to: Position, sand_positions: set[Position], max_row: int) -> bool:
    return to not in ROCKS and to not in sand_positions and to[0] < max_row


def iterate(sand_position: Position, sand_positions: set[Position], max_row: int) -> Position:
    i = sand_position[0] + 1
    down, left, right = (i, sand_position[1]), (i, sand_position[1] - 1), (i, sand_position[1] + 1)

    if is_allowed_to_go(down, sand_positions, max_row):
        sand_position = down
    elif is_allowed_to_go(left, sand_positions, max_row):
        sand_position = left
    elif is_allowed_to_go(right, sand_positions, max_row):
        sand_position = right
    else:
        sand_positions.add(sand_position)
        sand_position = START_POS

    return sand_position


def part1() -> int:
    max_row = max(ROCKS, key=operator.itemgetter(0))[0]
    min_col = min(ROCKS, key=operator.itemgetter(1))[1]
    max_col = max(ROCKS, key=operator.itemgetter(1))[1]

    sand_position, sand_positions = START_POS, set()
    while sand_position[0] <= max_row and min_col <= sand_position[1] <= max_col:
        sand_position = iterate(sand_position, sand_positions, max_row)

    return len(sand_positions)


def part2() -> int:
    max_row = max(ROCKS, key=operator.itemgetter(0))[0] + 2

    sand_position, sand_positions = START_POS, set()
    while sand_position[0] <= max_row and START_POS not in sand_positions:
        sand_position = iterate(sand_position, sand_positions, max_row)

    return len(sand_positions)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
