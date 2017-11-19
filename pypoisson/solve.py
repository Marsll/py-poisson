# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 11:56:18 2017

@author: Leon
"""

import numpy as np


def create_laplacian_2d(shape):
    laplacian = np.zeros((*shape, *shape))
    for k in range(0, shape[0]):
        for l in range(0, shape[1]):
            laplacian[k,l,k,l] = -4
            laplacian[(k+1) % shape[0],l,k,l] = 1
            laplacian[k-1,l,k,l] = 1
            laplacian[k,(l+1) % shape[1],k,l] = 1
            laplacian[k,l-1,k,l] = 1
    laplacian = np.reshape(laplacian, (shape[0]*shape[1], shape[0]*shape[1]) )               
    return laplacian

def solve(rho, epsilon = 0.1 , h = [0.1, 0.2]):
    return np.linalg.solve(create_laplacian_2d(rho.shape, , epsilon = 0.1 , h = [0.1, 0.2]), - np.reshape(rho, rho.shape[0] * rho.shape[1]))

    
