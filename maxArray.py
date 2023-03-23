# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:35:39 2023

@author: priya
"""

def maxArray(arr):
    sum1= 0
    for i in arr:
        if i>= sum1:
            sum1=i
    return sum1

print(maxArray([7,2,5,3,9,17,24,6,7,0,9]))