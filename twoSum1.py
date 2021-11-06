# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:03:36 2021

@author: priya
"""

def twoSum(arr,target):
    dict1 = {}
    count = 1
    for i in arr:
        if target-i in dict1:
            return [dict1[target-i],count]
        else:
            dict1[i] = count
        count += 1
        
        
print(twoSum([2,11,7,15],13))