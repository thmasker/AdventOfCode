import re


def setup_lights() -> list[list[int]]:
    return [[0 for _ in range(1000)] for _ in range(1000)]


def count_on_lights(lights: list[list[int]]) -> int:
    return sum([sum(lights_row) for lights_row in lights])


def turn_lights_part1(lights: list[list[int]], x_range: tuple[int, int], y_range: tuple[int, int],
                      brightness: int = None):
    for x in range(x_range[0], x_range[1]):
        for y in range(y_range[0], y_range[1]):
            if brightness is None:
                lights[x][y] = 0 if lights[x][y] else 1
            else:
                lights[x][y] = brightness


def part1():
    lights = setup_lights()

    for line in open('input.txt').readlines():
        coordinates = list(map(int, re.findall(r'\d+', line)))
        x_range, y_range = (coordinates[0], coordinates[2] + 1), (coordinates[1], coordinates[3] + 1)
        if line.startswith('turn on'):
            turn_lights_part1(lights, x_range, y_range, 1)
        elif line.startswith('turn off'):
            turn_lights_part1(lights, x_range, y_range, 0)
        elif line.startswith('toggle'):
            turn_lights_part1(lights, x_range, y_range)

    return count_on_lights(lights)


def turn_lights_part2(lights: list[list[int]], x_range: tuple[int, int], y_range: tuple[int, int], brightness: int):
    for x in range(x_range[0], x_range[1]):
        for y in range(y_range[0], y_range[1]):
            lights[x][y] = max(0, lights[x][y] + brightness)


def part2():
    lights = setup_lights()

    for line in open('input.txt').readlines():
        coordinates = list(map(int, re.findall(r'\d+', line)))
        x_range, y_range = (coordinates[0], coordinates[2] + 1), (coordinates[1], coordinates[3] + 1)
        if line.startswith('turn on'):
            turn_lights_part2(lights, x_range, y_range, 1)
        elif line.startswith('turn off'):
            turn_lights_part2(lights, x_range, y_range, -1)
        elif line.startswith('toggle'):
            turn_lights_part2(lights, x_range, y_range, 2)

    return count_on_lights(lights)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
