# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:22:24 2022

@author: priya
"""

def transposematrix(mat):
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i]= mat[j][i],mat[i][j]
    return mat 


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
    

def matrixRotation1(mat):
    mat = transposematrix(mat)
    mat = rotateColumn(mat)
    print(mat)
    
def matrixRotation2(mat):
    mat = rotateColumn(mat)
    mat = transposematrix(mat)
    print(mat)
    
    
    
matrixRotation1([[1,2,3],[4,5,6],[7,8,9]])
    
matrixRotation2([[1,2,3],[4,5,6],[7,8,9]])
    
    