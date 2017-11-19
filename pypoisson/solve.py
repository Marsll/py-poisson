# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:56:18 2017

@author: Leon
"""

import numpy as np


def solve(f, rho, epsilon=0.1, h=[0.1, 0.2]):
    laplacian = f(rho.shape, h)
    shape = np.asarray(rho.shape)
    rho_ = np.reshape(rho, np.prod(shape))
    return np.linalg.solve(laplacian, - rho_ / epsilon)
