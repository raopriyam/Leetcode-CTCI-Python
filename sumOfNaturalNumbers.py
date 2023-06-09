# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:02:33 2023

@author: priya
"""

def sumNaturalNumbers(n):
    sum1 = 0
    for i in range(n+1):
        sum1 = sum1 + i
        
    return sum1

print(sumNaturalNumbers(27))
        