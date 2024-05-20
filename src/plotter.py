from matplotlib import pyplot
from point import Point
from cluster import Cluster


class Plotter:
    colors = {
        "mean": "red",
        "center": "m"
    }

    @staticmethod
    def plot_points(lst: list):
        if type(lst[0]) is Point:
            Plotter._plot_single_cluster(lst)
        elif type(lst[0]) is Cluster:
            Plotter._plot_multiple_clusters(lst)

    @staticmethod
    def _plot_single_cluster(points: list):
        x = [point.x for point in points]
        y = [point.y for point in points]

        pyplot.scatter(list(x), list(y))
        pyplot.show()

    @staticmethod
    def _plot_multiple_clusters(clusters: list):
        for cluster in clusters:
            x = [point.x for point in cluster.points]
            y = [point.y for point in cluster.points]

            pyplot.scatter(x, y)
            mean = cluster.mean
            pyplot.scatter(mean.x, mean.y, color=Plotter.colors["mean"])
            center = cluster.center
            pyplot.scatter(center.x, center.y, color=Plotter.colors["center"])

        pyplot.show()

    @staticmethod
    def plot_graph(x, y):
        pyplot.plot(x, y)
        pyplot.show()

