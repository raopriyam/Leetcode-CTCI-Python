# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:33:21 2022

@author: priya
"""

def transposematrix(mat):
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i]= mat[j][i],mat[i][j]
    return mat 

print(transposematrix([[1,2,3],[4,5,6],[7,8,9]]))
            
            