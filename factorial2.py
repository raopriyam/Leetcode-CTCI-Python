# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 23:22:55 2023

@author: priya
"""

def factorial2(n):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)
    
print(factorial2(5))