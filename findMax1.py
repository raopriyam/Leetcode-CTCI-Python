# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 23:42:23 2025

@author: priya
"""

def findMax(arr):
    maxElement = float('-inf')
    for i in arr:
        if i > maxElement:
            maxElement = i
            
    return maxElement 


print(findMax([1,8,7,5,4,6,3,2]))