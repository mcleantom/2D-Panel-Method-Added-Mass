# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:29:53 2020

@author: mclea
"""
from stl import mesh as stl_mesh
from matplotlib import pyplot as plt
from hull_slicer.stl_slicer import make_slice
from vortexpanel import VortexPanel as vp
import numpy as np

file_loc = "data\\models\\5s.stl"

obj = stl_mesh.Mesh.from_file(file_loc)

plane_normal = [1, 0, 0]  # The plane normal vector
plane_origin = [0, 0, 0]  # A point on the plane
plane = [plane_origin, plane_normal]  # A plane facing right

hull_slice = make_slice(obj, plane)

x = np.flip(hull_slice.slice_points[:, 1])
y = np.flip(hull_slice.slice_points[:, 2])

geom = vp.panelize(x, y) # vp.make_spline(101, x, y, sharp=True)

alpha = np.pi/2
geom.solve_gamma(alpha)
geom.plot_flow(size=0.2)