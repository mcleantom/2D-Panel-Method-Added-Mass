# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:41:44 2020

@author: mclea
"""

import numpy as np
from stl import mesh as stl_mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt

file_loc = "5s.stl"
#
#figure = pyplot.figure()
#axes = mplot3d.Axes3D(figure)
#
obj = stl_mesh.Mesh.from_file(file_loc)
#axes.add_collection3d(mplot3d.art3d.Poly3DCollection(obj.vectors))
#scale = obj.points.flatten(-1)
#axes.auto_scale_xyz(scale, scale, scale)

plane_normal = [1,0,0] # The plane normal vector
plane_origin = [-0.8,0,0] # A point on the plane

plane = [plane_origin, plane_normal]  # A plane facing right

distance_from_plane = np.dot((obj.vectors-plane[0]), plane[1])

v0 = np.vstack(np.sign(distance_from_plane[:, 0] * distance_from_plane[:, 1]))
v1 = np.vstack(np.sign(distance_from_plane[:, 1] * distance_from_plane[:, 2]))
v2 = np.vstack(np.sign(distance_from_plane[:, 2] * distance_from_plane[:, 0]))

goes_through = np.concatenate([v0, v1, v2], 1)
# If the value is 0, the vector lies on the plane
# If the value is 1, the vector is completely off the plane
# If the value is -1, the vector goes through the plane
num_points = np.sum(goes_through == 0) * 2 + np.sum(goes_through == -1)

slice_points = np.zeros((num_points, 3))
curr_point = 0

for i in range(len(goes_through)):
    for x in range(len(goes_through[i])):
        if goes_through[i][x] == -1:
            # The line goes through the plane
            # There is a point which lies in the plane, which is r amounts 
            # of vector V away from point P0
            p0 = obj.vectors[i][x]
            if x == 0 or x==1:
                V = obj.vectors[i][x]-obj.vectors[i][x+1]
            else:
                V = obj.vectors[i][x]-obj.vectors[i][0]
            d = np.dot((plane_origin-p0), plane_normal)/(np.dot(V, plane_normal))
            P = p0 + d*V
            print(P)
            slice_points[curr_point] = P
            curr_point += 1
        
        if goes_through[i][x] == 0:
            # Both points on the line lie exaclty on the plane
            if x==0 or x==1:
                print(obj.vectors[i][x], obj.vectors[i][x+1])
                slice_points[curr_point] = obj.vectors[i][x]
                slice_points[curr_point+1] = obj.vectors[i][x+1]
            else:
                print(obj.vectors[i][x], obj.vectors[i][0])
                slice_points[curr_point] = obj.vectors[i][x]
                slice_points[curr_point+1] = obj.vectors[i][x+1]
            
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(slice_points[:,0], slice_points[:,1], slice_points[:,2])
#pyplot.plot()
