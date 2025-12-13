# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:36:42 2025

@author: priya
"""

def firstNNaturalNumSum(n):
    sum1 = 0
    for i in range(0,n+1):
        sum1 = sum1 + i
    return sum1 


print(firstNNaturalNumSum(6))