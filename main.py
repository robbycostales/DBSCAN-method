# Author: Robert Costales
# Language: Python 3
# Date: 4/24/2017
# Summary: This program analyzes three different datasets, and attempts to group
# them into the intended clusters using DBSCAN

import time as t
import csv
import numpy as np
from scipy.spatial import distance
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.group = 0 # unreachable points are -1
        self.visit = False


def DBSCAN (points, points_min, radius_max, data_name, debplot = False):
    """
    Args:
        points : list of objects belonging to point class defined above
        radius_max : set max radius for bubble
        points_min : minimum number of points needed for reacheable status
    """
    # init group number, will be increased for each loop
    cur_num = 0

    # for conversion to R
    # print("pre:", data_name)
    # r_x = []
    # r_y = []
    # r_visit = []
    # r_group = []
    # for i in points:
    #     r_x.append(i.x)
    #     r_y.append(i.y)
    #     r_visit.append(i.visit)
    #     r_group.append(i.group)
    # print("x: {0}\ny: {1}\nvisit: {2}\ngroup: {3}\n".format(r_x, r_y, r_visit, r_group))

    while True:
        # find unvisited point to work with
        cur_num += 1
        points_left = False
        for i in points:
            if i.visit == False:
                point = i
                points_left = True
                break
        # break if we visited all points
        if points_left == False:
            break

        # find all points within radius
        rad_points = []
        groups_to_convert = []
        for i in points:
            if distance.euclidean([point.x, point.y], [i.x, i.y]) < radius_max:
                rad_points.append(i)
                if not(i.group in groups_to_convert) and i.group != 0:
                    groups_to_convert.append(i.group)


        # if enough points, switch all to new group
        if len(rad_points) > points_min:
            for j in rad_points:
                j.visit = True
                j.group = cur_num
            # convert overlapping groups
            for j in points:
                if j.group in groups_to_convert:
                    j.group = cur_num
        else:
            point.visit = True
            point.group = -1


    if debplot == True:
        # convert to easier group numbers
        groups_to_convert = []
        for i in points:
            if not(i.group in groups_to_convert) and i.group != -1:
                groups_to_convert.append(i.group)
        for i in points:
            for j in range(len(groups_to_convert)):
                if i.group == groups_to_convert[j]:
                    i.group = j

        # clears plot
        plt.clf()

        # plotting
        colors = ["b", "g", "r", "c", "m", "y"]
        black = "k"
        for i in range(len(points)):
            if points[i].group != -1:
                color = colors[points[i].group % len(colors)]
            else:
                color = "k"
            plt.scatter(x=points[i].x, y=points[i].y, color=color)

        fig = plt.gcf()
        plt.title("{0} Clusters".format(data_name))
        fig.canvas.set_window_title("Cluster Plots")
        plt.show()

    # # for conversion to R
    # print("post:", data_name)
    # r_x = []
    # r_y = []
    # r_visit = []
    # r_group = []
    # for i in points:
    #     r_x.append(i.x)
    #     r_y.append(i.y)
    #     r_visit.append(i.visit)
    #     r_group.append(i.group)
    # print("x: {0}\ny: {1}\nvisit: {2}\ngroup: {3}\n".format(r_x, r_y, r_visit, r_group))


# moons data pre-processing
X, unused_statuses = make_moons(n_samples=200, noise=0.05, random_state=0)
x1 = [float(i[0]) for i in X]
y1 = [float(i[1]) for i in X]
# create point objects, store them in array
moons = []
for i in range(len(x1)):
    moons.append(Point(x1[i], y1[i]))

# circles data pre-processing
X, unused_statuses = make_circles(factor=0.4, n_samples=200, noise=0.05,
random_state=0)
x2 = [float(i[0]) for i in X]
y2 = [float(i[1]) for i in X]
# create point objects, store them in array
circles = []
for i in range(len(x2)):
    circles.append(Point(x2[i], y2[i]))

# blobs data pre-processing
X, unused_statuses = make_blobs(n_samples=200, cluster_std=1.0, shuffle=False, random_state=42)
x3 = [float(i[0]) for i in X]
y3 = [float(i[1]) for i in X]
# create point objects, store them in array
blobs = []
for i in range(len(x3)):
    blobs.append(Point(x3[i], y3[i]))

# call on all data sets
time = t.clock()
DBSCAN(moons, 2, .2, "Moon")
print(time - t.clock())
time = t.clock()
DBSCAN(circles, 2, .35, "Circle")
print(time - t.clock())
time = t.clock()
DBSCAN(blobs, 2, 2, "Blob")
print(time - t.clock())
time = t.clock()
