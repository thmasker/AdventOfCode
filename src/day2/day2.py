def part1() -> int:
    selection_score = {'X': 1, 'Y': 2, 'Z': 3}
    result_score = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }

    with open('input.txt', 'r') as file:
        score = 0
        for line in file:
            played = line.rstrip().split(' ')
            score += selection_score[played[1]] + result_score[played[0], played[1]]

    return score

def part2() -> int:
    result_score = {'X': 0, 'Y': 3, 'Z': 6}
    selection_score = {
        ('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
        ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
        ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
    }

    with open('input.txt', 'r') as file:
        score = 0
        for line in file:
            played = line.rstrip().split(' ')
            score += selection_score[(played[0], played[1])] + result_score[played[1]]

    return score

if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
