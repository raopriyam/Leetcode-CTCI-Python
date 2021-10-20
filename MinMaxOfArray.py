# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:17:24 2021

@author: priya
"""

def MinMax(arr):
    min1 = arr[0]
    max1 = arr[0]
    for i in arr:
        if i<min1:
            min1 = i
        if i>max1:
            max1 = i
    print("Min=",min1 )
    print("Max=",max1)
    

MinMax([1,3,5,-9,123,33,280,0])