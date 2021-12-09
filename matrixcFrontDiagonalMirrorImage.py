# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:44:35 2021

@author: priya
"""

def matrixcFrontDiagonalMirrorImage(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[j][i] 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()
            
matrixcFrontDiagonalMirrorImage([[1,2,3],[4,5,6],[7,8,9]])
