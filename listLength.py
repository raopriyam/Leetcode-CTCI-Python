# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 23:36:40 2025

@author: priya
"""

def listlength(arr):
    countLength = 0
    for i in arr:
        countLength += 1
        
    return countLength

print(listlength([1,3,2,4,6,77,88,5,0,9]))