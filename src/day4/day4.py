from typing import List


def to_int(numbers: List[str]) -> List[int]:
    return list(map(lambda x: int(x), numbers))


def part1() -> int:
    with open('input.txt', 'r') as file:
        overlaps = 0
        for line in file:
            line = line.split(',')
            a, b = to_int(line[0].split('-')), to_int(line[1].split('-'))
            if a[0] < b[0] and a[1] >= b[1] or a[0] == b[0] or a[0] > b[0] and a[1] <= b[1]:
                overlaps += 1
    return overlaps


def part2() -> int:
    with open('input.txt', 'r') as file:
        overlaps = 0
        for line in file:
            line = line.split(',')
            a, b = to_int(line[0].split('-')), to_int(line[1].split('-'))
            if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
                overlaps += 1
    return overlaps


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
