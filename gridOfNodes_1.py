# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:33:40 2021

@author: priya
"""

def collections(matrix):
    temp = 0
    sum1 = 0
    for i in matrix:
        count = 0
        #print(i)
        for j in i:
            if j == 1:
                count += 1
        if count > 0:
            sum1 = sum1 + temp*count
            temp = count
            
    return sum1


print(collections([[1,1,1],[0,1,0],[0,0,0],[1,1,0]]))