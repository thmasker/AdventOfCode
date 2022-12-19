from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Present:
    l: int
    w: int
    h: int

    def total_area(self):
        return self.area() + self.extra_area()

    def area(self):
        return 2 * self.l * self.w + 2 * self.w * self.h + 2 * self.l * self.h

    def extra_area(self):
        dimensions = self.get_dimensions()
        return dimensions[0] * dimensions[1]

    def ribbon_required(self):
        return self.bow_size() + self.perimeter()

    def bow_size(self):
        return self.l * self.w * self.h

    def perimeter(self):
        dimensions = self.get_dimensions()
        return 2 * dimensions[0] + 2 * dimensions[1]

    def get_dimensions(self):
        return sorted([self.l, self.h, self.w])

    @staticmethod
    def string_to_present(string: str) -> Present:
        matches = list(map(int, re.findall(r'\d+', string)))
        return Present(matches[0], matches[1], matches[2])


def get_presents():
    return [Present.string_to_present(line) for line in open('input.txt').readlines()]


if __name__ == '__main__':
    presents = get_presents()

    print(f'Part 1: {sum([present.total_area() for present in presents])}')
    print(f'Part 2: {sum([present.ribbon_required() for present in presents])}')
