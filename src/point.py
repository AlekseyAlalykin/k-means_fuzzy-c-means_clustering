import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def distance_from(self, point):
        x_dist = self.x - point.x
        y_dist = self.y - point.y
        return math.sqrt(x_dist*x_dist + y_dist*y_dist)