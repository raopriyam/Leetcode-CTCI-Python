# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:55:40 2022

@author: priya
"""

def concatenateArray(arr1):
    ans = arr1
    ans.extend(arr1)
    return ans

print(concatenateArray([1,2,3,1]))