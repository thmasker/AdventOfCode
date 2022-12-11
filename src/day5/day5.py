def parse_moves(lines: str) -> list[tuple[int, int, int]]:
    lines = lines.splitlines()
    moves = []
    for move in lines:
        move = move.split(' ')
        moves.append((int(move[1]), int(move[3]), int(move[5])))

    return moves


def part1() -> str:
    stacks = {
        1: ['W', 'M', 'L', 'F'],
        2: ['B', 'Z', 'V', 'M', 'F'],
        3: ['H', 'V', 'R', 'S', 'L', 'Q'],
        4: ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
        5: ['L', 'S', 'W'],
        6: ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
        7: ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
        8: ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
        9: ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']
    }

    for move in parse_moves(open('input.txt', 'r').read().split('\n\n')[1]):
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    return ''.join([value[-1] for _, value in stacks.items()])


def part2() -> str:
    stacks = {
        1: ['W', 'M', 'L', 'F'],
        2: ['B', 'Z', 'V', 'M', 'F'],
        3: ['H', 'V', 'R', 'S', 'L', 'Q'],
        4: ['F', 'S', 'V', 'Q', 'P', 'M', 'T', 'J'],
        5: ['L', 'S', 'W'],
        6: ['F', 'V', 'P', 'M', 'R', 'J', 'W'],
        7: ['J', 'Q', 'C', 'P', 'N', 'R', 'F'],
        8: ['V', 'H', 'P', 'S', 'Z', 'W', 'R', 'B'],
        9: ['B', 'M', 'J', 'C', 'G', 'H', 'Z', 'W']
    }

    for move in parse_moves(open('input.txt', 'r').read().split('\n\n')[1]):
        quantity = move[0]
        stacks[move[2]].extend(stacks[move[1]][-quantity:])
        stacks[move[1]] = stacks[move[1]][:len(stacks[move[1]]) - quantity]

    return ''.join([value[-1] for _, value in stacks.items()])


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
