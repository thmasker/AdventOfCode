import re


def part1():
    count = 0
    for line in open('input.txt').readlines():
        if not re.search('(ab)|(cd)|(pq)|(xy)', line) and re.search(r'([a-z])\1', line) and re.search('([aeiou].*){3,}',
                                                                                                      line):
            count += 1
    return count


def part2():
    count = 0
    for line in open('input.txt').readlines():
        if re.search(r'([a-z]).*\1', line) and re.search(r'([a-z])[a-z]\1', line):
            count += 1
    return count


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
