# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:37:32 2025

@author: priya
"""

def SumOfDigits(n):
    sum1 = 0
    while n > 0:
        r = n%10
        sum1 = sum1 + r
        n =int( n/10)
        
    return sum1


print(SumOfDigits(135))
        