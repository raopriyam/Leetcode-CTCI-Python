# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:43:55 2021

@author: priya
"""

def zeroMatrix(matrix):
    is_zero = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                is_zero.append((i, j))
    for x,y in is_zero:
        for j in range(len(matrix[0])):
            matrix[x][j] = 0
        for i in range(len(matrix)):
            matrix[i][y] = 0
    #print(matrix)
    print(matrix)
    
zeroMatrix([[1, 0, 3], [4, 0, 6], [2, 8, 9]])