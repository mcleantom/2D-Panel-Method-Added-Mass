# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:29:53 2020

@author: mclea
"""
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from stl import mesh as stl_mesh
from matplotlib import pyplot as plt
from stl_slicer import make_slice
from vortexpanel import VortexPanel as vp

file_loc = "5s.stl"

obj = stl_mesh.Mesh.from_file(file_loc)

plane_normal = [1, 0, 0]  # The plane normal vector
plane_origin = [0, 0, 0]  # A point on the plane
plane = [plane_origin, plane_normal]  # A plane facing right

hull_slice = make_slice(obj, plane)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(hull_slice.slice_points[:, 0],
           hull_slice.slice_points[:, 1],
           hull_slice.slice_points[:, 2])
