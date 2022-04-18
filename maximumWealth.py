# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:02:11 2022

@author: priya
"""

def maximumWealth(arr):
    sum1 = 0
    sumnum = 0
    for arr1 in arr:
        if sum(arr1) >= sum1:
            sum1= sum(arr1)
            sumnum = sumnum + 1
            
    return sum1

print(maximumWealth([[1,2,3],[2,3,1]]))

print(maximumWealth([[1,5],[7,3],[3,5]]))
            
print(maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
            
    