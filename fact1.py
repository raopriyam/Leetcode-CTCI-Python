# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 23:12:26 2023

@author: priya
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
        
print(fact(4))