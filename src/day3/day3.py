from itertools import zip_longest

def get_priority_sum(letters: list[chr]) -> int:
    priority_sum = 0
    for letter in letters:
        if 'a' <= letter <= 'z':
            priority_sum += ord(letter) - 96
        else:
            priority_sum += ord(letter) - 38
    return priority_sum


def find_common_letters(*compartments: str) -> set[chr]:
    return set.intersection(*[set(compartment) for compartment in compartments])


def part1() -> int:
    with open('input.txt', 'r') as file:
        common_letters = []
        for line in file:
            mid = len(line) // 2
            common_letters.extend(find_common_letters(line[:mid], line[mid:]))
    return get_priority_sum(common_letters)


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)


def part2() -> int:
    with open('input.txt', 'r') as file:
        common_letters = []
        for group in grouper(file, 3):
            common_letters.extend(find_common_letters(*[line.rstrip() for line in group]))

    return get_priority_sum(common_letters)


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
