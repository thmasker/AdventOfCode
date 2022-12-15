def create_grid() -> list[list[int]]:
    lines = [line.rstrip() for line in open('input.txt', 'r').readlines()]
    grid = []
    for i in range(len(lines)):
        row = []
        for j in range(len(lines[i])):
            row.append(int(lines[i][j]))
        grid.append(row)
    return grid


def edge_trees(grid: list[list[int]]) -> int:
    return 2 * (len(grid) + len(grid[0]) - 2)


def get_horizontal_trees(grid: list[list[int]], trees_positions: set[tuple[int, int]]):
    for y in range(1, len(grid) - 1):
        row = grid[y]
        max_height_left = row[0]
        for x in range(1, len(row) - 1):
            if row[x] > max_height_left:
                max_height_left = row[x]
                trees_positions.add((y, x))

        max_height_right = row[len(row) - 1]
        for x in range(len(row) - 2, 0, -1):
            if row[x] > max_height_right:
                max_height_right = row[x]
                trees_positions.add((y, x))


def get_vertical_trees(grid: list[list[int]], trees_positions: set[tuple[int, int]]):
    for x in range(1, len(grid[0]) - 1):
        max_height_up = grid[0][x]
        for y in range(1, len(grid) - 1):
            if grid[y][x] > max_height_up:
                max_height_up = grid[y][x]
                trees_positions.add((y, x))

        max_height_down = grid[len(grid) - 1][x]
        for y in range(len(grid) - 2, 0, -1):
            if grid[y][x] > max_height_down:
                max_height_down = grid[y][x]
                trees_positions.add((y, x))


def inner_trees(grid: list[list[int]]) -> int:
    trees_positions = set()
    get_horizontal_trees(grid, trees_positions)
    get_vertical_trees(grid, trees_positions)
    return len(trees_positions)


def part1() -> int:
    grid = create_grid()
    return edge_trees(grid) + inner_trees(grid)


def get_vertical_score(height: int, grid: list[list[int]], x: int, start: int, finish: int, step: int) -> int:
    score = 0
    for y in range(start, finish, step):
        if grid[y][x] < height:
            score += 1
        elif grid[y][x] == height:
            score += 1
            break
        else:
            break
    return score


def get_horizontal_score(height: int, row: list[int], start: int, finish: int, step: int) -> int:
    score = 0
    for x in range(start, finish, step):
        if row[x] < height:
            score += 1
        elif row[x] == height:
            score += 1
            break
        else:
            break
    return score


def part2() -> int:
    grid = create_grid()
    max_score = 0
    for y in range(1, len(grid)):
        for x in range(1, len(grid[0])):
            height = grid[y][x]
            scenic_score = get_vertical_score(height, grid, x, y - 1, -1, -1) * \
                           get_vertical_score(height, grid, x, y + 1, len(grid), 1) * \
                           get_horizontal_score(height, grid[y], x + 1, len(grid[y]), 1) * \
                           get_horizontal_score(height, grid[y], x - 1, -1, -1)
            if scenic_score > max_score:
                max_score = scenic_score
    return max_score


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
