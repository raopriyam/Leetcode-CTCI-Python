# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:38:27 2025

@author: priya
"""

def findLargestNum(arr):
    arr.sort()
    return arr[-1]


print(findLargestNum([4,2,7,9,1,3,5,6,8]))