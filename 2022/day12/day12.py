def get_adjacent_positions(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    adjacent_nodes = []
    if i > 0:
        adjacent_nodes.append((i - 1, j))
    if i < len(grid) - 1:
        adjacent_nodes.append((i + 1, j))
    if j > 0:
        adjacent_nodes.append((i, j - 1))
    if j < len(grid[i]) - 1:
        adjacent_nodes.append((i, j + 1))
    return adjacent_nodes


def parse_input() -> tuple[list[list[int]], tuple[int, int], tuple[int, int]]:
    grid = []
    start, end = (0, 0), (0, 0)
    with open('input.txt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            row = []
            for j in range(len(lines[i])):
                char = lines[i][j]
                if char == 'S':
                    char = 'a'
                    start = i, j
                elif char == 'E':
                    char = 'z'
                    end = i, j
                row.append(ord(char))
            grid.append(row)
    return grid, start, end


def find_positions(value: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                nodes.append((i, j))
    return nodes


def breadth_first_search(start: tuple[int, int], end: tuple[int, int], grid) -> int:
    to_visit, visited = [(start[0], start[1], 0)], set()
    while to_visit:
        i, j, distance = to_visit.pop(0)
        if (i, j) == end:
            return distance

        for ii, jj in get_adjacent_positions(i, j, grid):
            if (ii, jj) not in visited and grid[ii][jj] <= grid[i][j] + 1:
                visited.add((ii, jj))
                to_visit.append((ii, jj, distance + 1))


def part1() -> int:
    grid, start, end = parse_input()
    return breadth_first_search(start, end, grid)


def part2() -> int:
    grid, _, end = parse_input()
    return min(list(filter(lambda distance: distance,
                           [breadth_first_search(node, end, grid) for node in find_positions(ord('a'), grid)])))


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
