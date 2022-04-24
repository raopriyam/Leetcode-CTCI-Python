# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:36:29 2022

@author: priya
"""

def removeDuplicates(arr):
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    return arr

print(removeDuplicates([1,2,3,4,2,1,2,2,2,1,0,4,3,6,4,7,2,1,5,3,6,7,8]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    