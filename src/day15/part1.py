from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int

    def get_manhattan_distance(self, p2: tuple[int, int]) -> int:
        return abs(self.x - p2[0]) + abs(self.y - p2[1])


@dataclass
class Sensor(Point):
    beacon: Point

    def get_manhattan_distance_to_beacon(self) -> int:
        return abs(self.x - self.beacon.x) + abs(self.y - self.beacon.y)


def parse_input() -> list[Sensor]:
    sensors = []
    for line in open('input.txt').readlines():
        matches = list(map(int, re.findall('-?\d+', line)))
        sensors.append(Sensor(matches[0], matches[1], Point(matches[2], matches[3])))
    return sensors


def get_manhattan_distance(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def get_non_beacon_points(sensors: list[Sensor], y: int) -> set[Point]:
    non_beacon_points = set()
    for sensor in sensors:
        distance_to_beacon = sensor.get_manhattan_distance_to_beacon()
        vertical_distance = abs(y - sensor.y)
        if vertical_distance <= distance_to_beacon:
            x_distance = distance_to_beacon - vertical_distance
            for x in range(sensor.x - x_distance, sensor.x + x_distance + 1):
                non_beacon_points.add(Point(x, y))

    for sensor in sensors:
        if sensor.y == y:
            non_beacon_points.add(sensor)
        if sensor.beacon.y == y:
            non_beacon_points.difference_update({sensor.beacon})
    return non_beacon_points


# def get_non_beacon_points(sensors: list[Sensor], y: int) -> list[str]:
#     non_beacon_points = ['.' for _ in range(27)]
#     for sensor in sensors:
#         if sensor.y == y:
#             non_beacon_points[sensor.x + 2] = 'S'
#         if sensor.beacon.y == y:
#             non_beacon_points[sensor.beacon.x + 2] = 'B'
#
#     for sensor in sensors:
#         distance_to_beacon = sensor.get_manhattan_distance_to_beacon()
#         vertical_distance = abs(y - sensor.y)
#         if vertical_distance <= distance_to_beacon:
#             x_distance = distance_to_beacon - vertical_distance
#             for x in range(sensor.x - x_distance, sensor.x + x_distance + 1):
#                 if non_beacon_points[x + 2] == '.':
#                     non_beacon_points[x + 2] = '#'
#     return non_beacon_points


def part1(y: int) -> int:
    return len(get_non_beacon_points(parse_input(), y))


if __name__ == '__main__':
    print(f'Part 1: {part1(2_000_000)}')
