# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 23:50:33 2021

@author: priya
"""

def matrixcBackDiagonalMirrorImage(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[j][i] = mat[i][j] 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()
        
        
matrixcBackDiagonalMirrorImage([[1,2,3],[4,5,6],[7,8,9]])