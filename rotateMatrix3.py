# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:00:30 2023

@author: priya
"""

def rotateMatrix3(matrix):
    print(matrix)
    for i in range(len(matrix)):
        for j in range(i,len(matrix[0])):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix

print(rotateMatrix3([[1,2,3],[4,5,6],[7,8,9]]))