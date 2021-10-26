# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 23:04:49 2021

@author: priya
"""

def addArray(arr,val):
    for i in range(len(arr)):
        arr[i] = arr[i]+val
        print(arr[i])
    print(arr)
    
    
arr = [1,2,3,4,5]
addArray(arr,10)