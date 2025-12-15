# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:28:08 2025

@author: priya
"""

def largetsof3numbers(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
        
        
print(largetsof3numbers(5,9,8))