# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:24:39 2021

@author: priya
"""

def printMatrix(mat):
    for i in mat:
        for j in i:
            print(j,end=" ")
        print()
        
printMatrix([[1,2,3],[4,5,6],[7,8,9]])