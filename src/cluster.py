from point import Point


class Cluster:
    def __init__(self, center: Point, points: list):
        self.center = center
        self.points = points

    def add_point(self, point: Point):
        self.points.append(point)

    @property
    def mean(self):
        x_vals = [point.x for point in self.points]
        y_vals = [point.y for point in self.points]

        if len(self.points) == 0:
            return self.center
        else:
            return Point(sum(x_vals) / len(self.points), sum(y_vals) / len(self.points))

    def calc_variation(self):
        variation = 0
        for point in self.points:
            variation += point.distance_from(self.center)

        return variation

    def wcss(self):
        return sum([point.distance_from(self.center)**2 for point in self.points])

    def __eq__(self, other):
        if set(self.points) == set(other.points):
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)