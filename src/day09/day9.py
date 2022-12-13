class Knot:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class Head(Knot):
    def move(self, direction: chr):
        match direction:
            case 'R':
                self.x += 1
            case 'L':
                self.x -= 1
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1


class Tail(Knot):
    def __init__(self, x: int = 0, y: int = 0):
        super().__init__(x, y)
        self.visited_positions = set()

    def move(self, knot: Knot):
        x_distance, y_distance = knot.x - self.x, knot.y - self.y
        if abs(x_distance) == 2 and y_distance == 0:
            self.x += 1 if x_distance > 0 else -1
        elif abs(y_distance) == 2 and x_distance == 0:
            self.y += 1 if y_distance > 0 else -1
        elif abs(x_distance) == 2 and abs(y_distance) > 0 or abs(y_distance) == 2 and abs(x_distance) > 0:
            self.x += 1 if x_distance > 0 else -1
            self.y += 1 if y_distance > 0 else -1
        self.visited_positions.add((self.x, self.y))


def get_visited_positions(n_knots: int) -> int:
    moves = [line.rstrip().split(' ') for line in open('input.txt', 'r').readlines()]
    head = Head()
    tails = [Tail() for _ in range(n_knots - 1)]
    for move in moves:
        direction, quantity = move[0], int(move[1])
        for _ in range(quantity):
            head.move(direction)
            tails[0].move(head)
            for i in range(1, len(tails)):
                tails[i].move(tails[i - 1])
    return len(tails[-1].visited_positions)


if __name__ == '__main__':
    print(f'Part 1: {get_visited_positions(2)}')
    print(f'Part 2: {get_visited_positions(10)}')
