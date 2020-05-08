# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:29:53 2020

@author: mclea
"""
from stl import mesh as stl_mesh
# from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from stl_slicer import make_slice
from vortexpanel import VortexPanel as vp
import numpy as np

file_loc = "5s.stl"

obj = stl_mesh.Mesh.from_file(file_loc)

plane_normal = [1, 0, 0]  # The plane normal vector
plane_origin = [0, 0, 0]  # A point on the plane
plane = [plane_origin, plane_normal]  # A plane facing right

hull_slice = make_slice(obj, plane)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(hull_slice.slice_points[:, 0],
#           hull_slice.slice_points[:, 1],
#           hull_slice.slice_points[:, 2])

x = np.flip(hull_slice.slice_points[:, 1])
y = np.flip(hull_slice.slice_points[:, 2])

geom = vp.make_spline(500, x, y)
geom.plot('-o')

alpha = np.pi/2
geom.solve_gamma(alpha)
geom.plot_flow()
