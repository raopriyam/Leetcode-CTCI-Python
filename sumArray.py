# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 23:47:31 2022

@author: priya
"""

def sumArray(mat):
    res = 0 
    count = 0
    for i in mat:
        if sum(i)>res:
            res = sum(i)
        count= count + 1
    return res, count

print(sumArray([[1,2,3],[4,5,6],[7,8,9]]))