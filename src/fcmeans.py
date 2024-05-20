from random import random
from point import Point
from cluster import Cluster
import math


class FCMeans:
    def __init__(self, points, c_value, fuzziness=2, tolerance_value=0.001):
        self.fuzziness = fuzziness
        membership_matrix = [[] for i in range(0, c_value)]
        for i in range(0, len(points)):
            membership_vals = [random() for i in range(0, c_value)]
            membership_sum = sum(membership_vals)
            for j in range(0, c_value):
                membership_matrix[j].append(membership_vals[j]/membership_sum)

        difference = 1
        while difference > tolerance_value:
            cluster_centers = self.__get_cluster_centers(points, membership_matrix)
            new_membership_matrix = self.__get_membership_matrix(points, cluster_centers)
            difference = self.__calc_diff(membership_matrix, new_membership_matrix)
            membership_matrix = new_membership_matrix

        clusters = [Cluster(center, []) for center in cluster_centers]
        for i in range(0, len(points)):
            membership = [membership_matrix[j][i] for j in range(0, len(membership_matrix))]
            clusters[membership.index(max(membership))].add_point(points[i])

        self.clusters = clusters

    def __get_cluster_centers(self, points, membership_matrix):
        centers = []
        for i in range(0, len(membership_matrix)):
            x_val = sum([(membership_matrix[i][j] ** self.fuzziness) * points[j].x for j in range(0, len(points))])
            y_val = sum([(membership_matrix[i][j] ** self.fuzziness) * points[j].y for j in range(0, len(points))])
            x_val = x_val / sum([membership_matrix[i][j] ** self.fuzziness for j in range(0, len(points))])
            y_val = y_val / sum([membership_matrix[i][j] ** self.fuzziness for j in range(0, len(points))])

            centers.append(Point(x_val, y_val))

        return centers

    def __get_membership_matrix(self, points, centers):
        membership_matrix = [[] for i in range(0, len(centers))]

        for i in range(len(centers)):
            for j in range(len(points)):
                distances = [points[j].distance_from(center) for center in centers]
                new_membership_val = sum([(distances[i]**2) / (distances[k]**2) for k in range(0, len(centers))])
                new_membership_val = (new_membership_val ** (1/(self.fuzziness - 1))) ** -1

                membership_matrix[i].append(new_membership_val)

        return membership_matrix

    def __calc_diff(self, matrix_a, matrix_b):
        diff_vals = []
        for i in range(0, len(matrix_a)):
            for j in range(0, len(matrix_a[i])):
                diff_vals.append(abs(matrix_a[i][j] - matrix_b[i][j]))

        return max(diff_vals)

    def get_clusters(self):
        return self.clusters
