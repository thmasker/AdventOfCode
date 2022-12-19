def get_path():
    return open('input.txt').readline()


def new_position(position: tuple[int, int], char: chr) -> tuple[int, int]:
    x, y = position[0], position[1]
    if char == '^':
        y += 1
    elif char == '>':
        x += 1
    elif char == '<':
        x -= 1
    elif char == 'v':
        y -= 1
    return x, y


def part1():
    visited = {(0, 0)}
    x, y, houses = 0, 0, 1
    for char in get_path():
        x, y = new_position((x, y), char)
        visited.add((x, y))
    return len(visited)


def part2():
    visited = {(0, 0)}
    x, y, bot_x, bot_y, houses = 0, 0, 0, 0, 2
    for i, char in enumerate(get_path()):
        if i % 2 == 0:
            x, y = new_position((x, y), char)
            visited.add((x, y))
        else:
            bot_x, bot_y = new_position((bot_x, bot_y), char)
            visited.add((bot_x, bot_y))
    return len(visited)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
