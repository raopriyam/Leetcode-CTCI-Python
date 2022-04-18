# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:50:14 2022

@author: priya
"""

def buildArray(arr):
    res = []
    for i in arr:
        res.append(arr[i]) 
    return res

print(buildArray([0,2,1,5,3,4]))

print(buildArray([5,0,1,2,3,4]))


    