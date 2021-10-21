# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:18:40 2021

@author: priya
"""

def subArrayWithGivenSum(arr,sum1):
    dict1 = {}
    index = 0
    for i in arr:
        if i not in dict1:
            dict1[sum1-i] = index
        else:
            return([dict1[i],index])
        index += 1
        
print(subArrayWithGivenSum([1,2,3,5,7],12))
            