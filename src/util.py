from point import Point
from matplotlib import pyplot


def get_points(filename):
    points = []
    with open(filename) as file:
        for line in file:
            coords = line.split()
            points.append(Point(
                x=float(coords[0]),
                y=float(coords[1])
            ))

    return points


def plot_points(points: list):
    x = [point.x for point in points]
    y = [point.y for point in points]

    pyplot.scatter(x, y)
    pyplot.show()

