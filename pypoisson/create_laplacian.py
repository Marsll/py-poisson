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

#np.set_printoptions(threshold=np.inf)
#print(create_laplacian_2d((3,4)))

def create_laplacian_3d(shape):
    laplacian = np.zeros((*shape, *shape))
    for k in range(0, shape[0]):
        for l in range(0, shape[1]):
            for m in range(0, shape[2]):
                laplacian[k,l,m,k,l,m] = -4
                laplacian[(k+1) % shape[0],l,m,k,l,m] = 1
                laplacian[k-1,l,m,k,l,m] = 1
                laplacian[k,(l+1) % shape[1],m,k,l,m] = 1
                laplacian[k,l-1,m,k,l,m] = 1
                laplacian[k,l,(m+1) % shape[1],k,l,m] = 1
                laplacian[k,l,(m-1),k,l,m] = 1
    laplacian = np.reshape(laplacian, (shape[0] * shape[1] * shape[2], shape[0]*shape[1]*shape[2]))               
    return laplacian
 
np.set_printoptions(threshold=np.inf)
print(create_laplacian_3d((3,3,3)))

    