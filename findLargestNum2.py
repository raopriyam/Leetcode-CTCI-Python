# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:39:36 2025

@author: priya
"""

def FindLargetsNum(arr):
    maxNum = float('-inf')
    for i in arr:
        if i > maxNum:
            maxNum = i
            
    return maxNum


print(FindLargetsNum([4,2,7,9,1,3,5,6,8]))
    