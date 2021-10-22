# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:43:02 2021

@author: priya
"""

def missingNumber(arr):
    n = len(arr)
    sum1 = sum(arr)
    sum2 = sum(range(1,n+2))
    return sum2-sum1
    
    
    
print(missingNumber([1,2,3,5]))