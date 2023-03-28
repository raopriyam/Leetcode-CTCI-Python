# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:46:09 2023

@author: priya
"""

def rotateMatrix(matrix):
    print(matrix)
    for i in range(len(matrix)):
        for j in range(i,len(matrix[0])):
            matrix[i],matrix[j] = matrix[j],matrix[i]
    return matrix

print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))