def part1() -> int:
    floor = 0
    for char in open('input.txt').read():
        if char == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def part2() -> int:
    floor = 0
    for i, char in enumerate(open('input.txt').read()):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1
    return floor


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
