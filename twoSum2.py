# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:07:10 2021

@author: priya
"""

def twoSum2(arr,target):
    dict1 = {}
    count = 1
    i = 0
    while arr[i] <= target:
        if target-arr[i] in dict1:
            return [dict1[target-arr[i]],count]
        else:
            dict1[arr[i]] = count
        count += 1
        i += 1
        
print(twoSum2([2,7,11,15],9))