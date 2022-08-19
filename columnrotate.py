# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:32:36 2022

@author: priya
"""

def columnrotate(mat):
    for i in range(len(mat)):
        start = 0
        end= len(mat[0])-1
        while start<end:
            temp = mat[i][start]
            mat[i][start] = mat[i][end]
            mat[i][end] = temp 
            start = start+ 1
            end = end - 1
       #print(mat)
    return mat
print(columnrotate([[1,2,3],[4,5,6],[7,8,9]]))