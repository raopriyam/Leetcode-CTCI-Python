# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:31:12 2021

@author: priya
"""

def fact(n):
    sum1 = 1
    for i in range(2,n+1):
        sum1 = sum1*i
    return sum1


print(fact(12))