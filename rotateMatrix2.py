# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:55:19 2023

@author: priya
"""

def rotateMatrix2(matrix):
    print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i],matrix[j] = matrix[j],matrix[i]
    return matrix

print(rotateMatrix2([[1,2,3],[4,5,6],[7,8,9]]))