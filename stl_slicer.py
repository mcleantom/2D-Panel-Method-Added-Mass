# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:41:44 2020

@author: mclea
"""

import numpy as np
from stl import mesh as stl_mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

file_loc = "cube.stl.txt"

figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

obj = stl_mesh.Mesh.from_file(file_loc)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(obj.vectors))

scale = obj.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

pyplot.show()

plane = [[0, 0, 0], [1, 1, 1]]  # A plane facing right

distance_from_plane = np.dot((obj.vectors-plane[0]), plane[1])

AB = np.vstack(np.sign(distance_from_plane[:, 0] * distance_from_plane[:, 1]))
BC = np.vstack(np.sign(distance_from_plane[:, 1] * distance_from_plane[:, 2]))
CA = np.vstack(np.sign(distance_from_plane[:, 2] * distance_from_plane[:, 0]))

goes_through = np.concatenate([AB, BC, CA], 1)
# print(goes_through)
points = []
for i, n in enumerate(goes_through):
    for x, cut in enumerate(n):
        if cut == 0: # the vertex goes straight through the plane, can pick both points
            if x == 0:
                indexes = [0, 1]
            elif x == 1:
                indexes = [1, 2]
            else:
                indexes = [2, 0]
            points.append(obj.vectors[i][indexes])
#
#        if cut == -1:
#
print(points)
