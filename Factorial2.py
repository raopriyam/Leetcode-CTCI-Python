# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:30:44 2025

@author: priya
"""

def Factorial(n):
    sum1 = 1
    for i in range(1,n+1):
        sum1 = sum1*i
    
    return sum1


print(Factorial(6))