# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 23:45:34 2025

@author: priya
"""

def countFrequency(arr):
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    return dict1


print(countFrequency([1,2,3,1,4,2,3,5,4,1,6,7,5,8,0,9,67,5,7,6,89]))
        