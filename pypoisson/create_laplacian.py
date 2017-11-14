# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:01:01 2017

@author: Leon
"""

import numpy as np
"""
alternativ
def create_laplacian_1d(shape, h = 0.1):
    laplacian = -2 * np.identity(shape)
    for i in range(0, shape):
        laplacian[i][i - 1] = 1
        laplacian[i][(i + 1) % shape] = 1
    return laplacian
"""


def create_laplacian_1d(shape, h = 0.1):
    """Return Laplacian for one dimension"""
    laplacian = np.diag(-2 * np.ones(shape))
    laplacian += np.diag(np.ones(shape - 1), k = 1)
    laplacian += np.diag(np.ones(shape - 1), k = -1)
    #periodic boundary conditions
    laplacian[0][-1] += 1
    laplacian[-1][0] += 1
    return laplacian
    