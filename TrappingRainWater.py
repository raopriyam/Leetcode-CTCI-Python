# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:34:58 2024

@author: priya
"""

def maxArea(arr):
    res = 0
    for l in range(len(arr)):
        for r in range(l+1,len(arr)):
            area = (l-r)*min(arr[l],arr[r])
            res = max(res,area)
            
    return res

print(maxArea([1,8,6,2,5,4,8,3,7]))