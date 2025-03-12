from itertools import islice

from src.Vector import Vector


def next_n_lines(opened_file, n):
    return [line.split() for line in islice(opened_file, n)]


def get_start_end(c1, c2):
    return (c1, c2) if c1 <= c2 else (c2, c1)


vectors = []
table = []
overlaps = 0

with open("../input/day5.txt") as file:
    while vector := next_n_lines(file, 1):
        p1, p2 = vector[0][0], vector[0][2]
        (x1, y1), (x2, y2) = p1.split(','), p2.split(',')
        vectors.append(Vector(int(x1), int(y1), int(x2), int(y2)))

    x_max = max(max([vector.x1 for vector in vectors]), max([vector.x2 for vector in vectors]))
    y_max = max(max([vector.y1 for vector in vectors]), max([vector.y2 for vector in vectors]))
    max_len = max(x_max, y_max)

    table = [[0 for _ in range(max_len + 1)] for _ in range(max_len + 1)]

    for vector in vectors:
        if vector.is_horizontal():
            start, end = get_start_end(vector.y1, vector.y2)

            for y in range(start, end + 1):
                table[y][vector.x1] += 1
        elif vector.is_vertical():
            start, end = get_start_end(vector.x1, vector.x2)

            for x in range(start, end + 1):
                table[vector.y1][x] += 1

    for row in table:
        for col in row:
            if col >= 2:
                overlaps += 1

    print(overlaps)
