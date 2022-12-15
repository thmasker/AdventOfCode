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


def get_non_beacon_ranges(sensors: list[Sensor], y: int) -> set[tuple[int, int]]:
    non_beacon_points = set()
    for sensor in sensors:
        distance_to_beacon = sensor.get_manhattan_distance_to_beacon()
        vertical_distance = abs(y - sensor.y)
        if vertical_distance <= distance_to_beacon:
            x_distance = distance_to_beacon - vertical_distance
            non_beacon_points.add((sensor.x - x_distance, sensor.x + x_distance))

    beacons_in_y = set()
    for sensor in sensors:
        if sensor.beacon.y == y:
            beacons_in_y.add(sensor.beacon.x)

    for _, non_beacon_point in enumerate(non_beacon_points):
        for _, beacon_in_y in enumerate(beacons_in_y):
            if non_beacon_point[0] < beacon_in_y:
                if non_beacon_point[1] == beacon_in_y:
                    non_beacon_points.difference_update({non_beacon_point})
                    non_beacon_points.add((non_beacon_point[0], non_beacon_point[1] - 1))
                elif non_beacon_point[1] > beacon_in_y:
                    non_beacon_points.difference_update({non_beacon_point})
                    non_beacon_points.add((non_beacon_point[0], beacon_in_y - 1))
                    non_beacon_points.add((beacon_in_y + 1, non_beacon_point[1]))
            elif non_beacon_point[0] == beacon_in_y:
                if non_beacon_point[1] == beacon_in_y:
                    non_beacon_points.difference_update({non_beacon_point})
                elif non_beacon_point[1] > beacon_in_y:
                    non_beacon_points.difference_update({non_beacon_point})
                    non_beacon_points.add((beacon_in_y + 1, non_beacon_point[1]))

    # todo eliminar overlapping ranges
    return non_beacon_points


def part1(y: int) -> int:
    return get_non_beacon_ranges(parse_input(), y)


def part2(max_x: int) -> int:
    return 0


if __name__ == '__main__':
    print(f'Part 1: {part1(2_000_000)}')
    print(f'Part 2: {part2(20)}')
