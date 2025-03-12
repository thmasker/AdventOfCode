def parse() -> tuple[list[int], list[int], dict[int, int]]:
    left_n, right_n, rights = [], [], {}
    with open('input.txt') as f:
        for line in f:
            numbers = line.strip().split('   ')
            left_n.append(int(numbers[0]))
            right_n.append(int(numbers[1]))
            right = int(numbers[1])
            if right in rights:
                rights[right] += 1
            else:
                rights[right] = 1
    return left_n, right_n, rights


def part1() -> int:
    lefts, rights, _ = parse()
    lefts.sort()
    rights.sort()
    return sum([abs(lefts[i] - rights[i]) for i in range(len(lefts))])


def part2() -> int:
    lefts, _, rights = parse()
    return sum([n * rights.get(n, 0) for n in lefts])


if __name__ == '__main__':
    print(part1())
    print(part2())
