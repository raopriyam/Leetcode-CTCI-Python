# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:53:55 2021

@author: priya
"""

def collections(matrix):
    list1 = []
    for i in matrix:
        a = i.count(1)
        list1.append(a)
    #print(list1)
    sum1 = 0
            
    for i in range(len(list1)-1):
        if list1[i] == 0:
            
        else:
            sum1 = sum1 + list1[i] * list1[i+1]
    return sum1
    


print(collections([[1,1,1],[0,1,0],[0,0,0],[1,1,0]]))