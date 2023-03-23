# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:38:05 2023

@author: priya
"""
import math

def minArray(arr):
    min1 = math.inf
    for i in arr:
        if min1 >= i:
            min1 = i
    return min1

print(minArray([2,4,0,8,9,6,1,7]))
    
    