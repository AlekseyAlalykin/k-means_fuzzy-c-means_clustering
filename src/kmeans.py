import random
from cluster import Cluster


class KMeans:
    def __init__(self, points, k_value, attempts=10):
        clustering_results = []
        for i in range(0, attempts):
            tmp_clusters = None
            clusters = []
            for item in random.sample(points, k_value):
                clusters.append(Cluster(item, []))

            while True:
                for point in points:
                    cluster_dist = []
                    for cluster in clusters:
                        cluster_dist.append(point.distance_from(cluster.center))

                    clusters[cluster_dist.index(min(cluster_dist))].add_point(point)

                #Если первый проход
                if tmp_clusters is None:
                    tmp_clusters = clusters
                    clusters = [Cluster(cluster.mean, []) for cluster in clusters]
                else:
                    equal = True
                    for i in range(0, len(clusters)):
                        if tmp_clusters[i] != clusters[i]:
                            equal = False
                            break

                    # Если кластеры не отличаются
                    if equal:
                        break
                    else:
                        tmp_clusters = clusters
                        clusters = [Cluster(cluster.mean, []) for cluster in clusters]

            clustering_results.append(clusters)

        variations = []
        for clusters in clustering_results:
            variation = 0
            for cluster in clusters:
                variation += cluster.calc_variation()
            variations.append(variation)

        self.clusters = clustering_results[variations.index(min(variations))]

    def get_cluster_points(self):
        return [cluster.points for cluster in self.clusters]

    def get_clusters(self):
        return self.clusters

    def get_k_value(self):
        return len(self.clusters)

    def calc_variation(self):
        return sum([cluster.calc_variation() for cluster in self.clusters])

    def wcss(self):
        return sum([cluster.wcss() for cluster in self.clusters])



