# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:58:55 2022

@author: priya
"""

def runningSum(arr1):
    sum1 = 0
    ans = []
    for i in arr1:
        sum1 = sum1 + i
        ans.append(sum1)
    return ans
    

print(runningSum([1,2,3,4]))

print(runningSum([1,1,1,1,1]))