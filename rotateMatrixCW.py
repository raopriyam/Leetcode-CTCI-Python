# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:46:44 2022

@author: priya
"""

def rotateRow(mat):
    start = 0
    end = len(mat) - 1
    while start<end:
        temp = mat[start]
        mat[start] = mat[end]
        mat[end] = temp
        start = start + 1
        end = end - 1
    return mat 


def rotateColumn(mat):
    for i in range(len(mat)):
        start = 0
        end = len(mat[0])-1
        while start<end:
            temp = mat[i][start]
            mat[i][start] = mat[i][end]
            mat[i][end] = temp
            start = start + 1
            end = end - 1
    return mat
    
        
    

def rotatematrixcw(mat): 
    print(mat)
    res = rotateRow(mat)
    print(res)
    res1 = rotateColumn(res)
    print(res1)
    return res1

print(rotatematrixcw([[1,2,3],[4,5,6],[7,8,9]]))
    