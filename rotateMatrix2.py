# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 23:37:14 2022

@author: priya
"""

def rotateMatrix2(mat):
    
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    return mat

print(rotateMatrix2([[1,2,3],[4,5,6],[7,8,9]]))