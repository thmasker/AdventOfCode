import re
from operator import itemgetter

from joblib import Parallel, delayed

Point = tuple[int, int]


def parse_input() -> list[tuple[Point, Point]]:
    sensors = []
    for line in open('input.txt').readlines():
        matches = list(map(int, re.findall(r'-?\d+', line)))
        sensors.append(((matches[0], matches[1]), (matches[2], matches[3])))
    return sensors


def get_manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_row(beacons: set[int], row_at_y: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not beacons:
        return row_at_y

    row = []
    for start, end in row_at_y:
        for beacon in beacons:
            if start < beacon < end:
                row.append((start, beacon - 1))
                row.append((beacon + 1, end))
            elif start == beacon:
                row.append((beacon + 1, end))
            elif end == beacon:
                row.append((start, beacon - 1))
            elif beacon < start or beacon > end:
                row.append((start, end))
    return row


def get_row_at_y(sensors: list[tuple[Point, Point]], y: int, without_beacons: bool = True, min_x: int = float('-inf'),
                 max_x: int = float('inf')) -> list[tuple[int, int]]:
    row_at_y = []
    for sensor, beacon in sensors:
        distance_to_beacon = get_manhattan_distance(sensor, beacon)
        vertical_distance = abs(y - sensor[1])
        if vertical_distance <= distance_to_beacon:
            x_distance = distance_to_beacon - vertical_distance
            start, end = sensor[0] - x_distance, sensor[0] + x_distance
            if start >= min_x or end <= max_x:
                row_at_y.append((start, end))

    return get_row({beacon[0] for _, beacon in sensors if beacon[1] == y}, row_at_y) if without_beacons else row_at_y


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort()
    merged = [intervals[0]]
    for interval in intervals[1:]:
        if merged[-1][0] <= interval[0] <= merged[-1][-1]:
            merged[-1] = (merged[-1][0], max(merged[-1][-1], interval[-1]))
        else:
            merged.append(interval)
    return merged


def part1(y: int) -> int:
    non_beacon_points = 0
    for start, end in merge_intervals(get_row_at_y(parse_input(), y)):
        non_beacon_points += end - start + 1

    return non_beacon_points


def get_row_result(sensors, y, max_coordinate):
    row = merge_intervals(get_row_at_y(sensors, y, without_beacons=False, min_x=0, max_x=max_coordinate))
    current_x = row[0]
    for start, end in row[1:]:
        if start - current_x[1] == 2:
            return (start - 1) * 4_000_000 + y
        current_x = (start, end)


def part2(max_coordinate: int) -> int:
    sensors = parse_input()
    rows = Parallel(n_jobs=-1)(delayed(get_row_result)(sensors, y, max_coordinate) for y in range(max_coordinate + 1))
    return max(list(filter(lambda x: x, rows)))


if __name__ == '__main__':
    print(f'Part 1: {part1(2_000_000)}')
    print(f'Part 2: {part2(4_000_000)}')
