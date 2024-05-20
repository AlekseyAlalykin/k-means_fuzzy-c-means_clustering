import random

import util
from kmeans import KMeans
from fcmeans import FCMeans
from plotter import Plotter
from point import Point


def elbow_method(points):
    K = range(2, 10)
    cluster_wcss = []
    for k in K:
        kmeans = KMeans(points, k)
        cluster_wcss.append(kmeans.wcss())

    Plotter.plot_graph(K, cluster_wcss)


def main():
    points = util.get_points("test_data/data3.txt")
    fcmeans = FCMeans(points, 5)
    Plotter.plot_points(fcmeans.get_clusters())


if __name__ == '__main__':
    main()
