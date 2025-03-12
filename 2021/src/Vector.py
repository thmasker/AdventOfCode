import math


class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_horizontal(self):
        return self.x1 == self.x2

    def is_vertical(self):
        return self.y1 == self.y2
