# -*- coding: utf-8 -*-
"""
This class takes a stl object and can slice it at any plane to create a 2D
cross section.

Classes:

Methods:

Imports:
    numpy
"""

import numpy as np


class pannels():
    """
    

    Attributes:
        slice_points    --  An array of all the points in a slice of the stl
                            object
    """

    def __init__(self, x_coords, y_coords):
        """
        Initialises the connect_points class

        Inputs:
 
        Outputs:
            An array of lines that make a hull form from a sliced hull
        """
        self.lines = np.zeros((len(x_coords), 2))
