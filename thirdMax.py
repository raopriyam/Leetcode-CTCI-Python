# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 02:02:27 2025

@author: priya
"""

def thirdMax(nums):
    set1 = set(nums)
    set1 = sorted(set1)

    if len(set1) >= 3:
        return set1[-3]
    else:
        return set1[-1]
    
print(thirdMax([1,2,3]))