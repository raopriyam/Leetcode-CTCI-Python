# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 22:41:40 2021

@author: priya
"""

def firstRepeatingInteger(arr):
    dict1 = {}
    count = 0
    for i in arr:
        if i in dict1:
            return dict1[i]
        else:
            dict1[i] = count
        count += 1
    return None
     

print(firstRepeatingInteger([1, 5, 3, 4, 3, 5, 6]))

print(firstRepeatingInteger([1, 2, 3, 4]))