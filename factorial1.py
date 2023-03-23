# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:16:44 2023

@author: priya
"""

def factorial(n):
    if n<0:
        return "factorial doesn't exist"
    elif n==0:
        return 1
    else:
        sum1 = 1
        for i in range(1,n+1):
            sum1 = sum1 * i
        return sum1

print(factorial(5))