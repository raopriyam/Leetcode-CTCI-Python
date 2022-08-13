# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:36:09 2022

@author: priya
"""

def matrixrowreverse(mat):
    len1 = int(len(mat)/2)
    j = -1
    for i in range(len1):
        mat[i] ,mat[j] = mat[j],mat[i]
        j = j-1
    return mat 

print(matrixrowreverse([[1,2,3],[4,5,6],[7,8,9],[0,1,0]]))
        