# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:07:24 2021

@author: priya
"""

def firstNonRepeatingInteger(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    return None


print(firstNonRepeatingInteger([-1, 2, -1, 3, 2]))

print(firstNonRepeatingInteger([1, 1, 1]))

