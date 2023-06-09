# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:51:39 2023

@author: priya
"""

def checkNumber(n):
    if n>0:
        return "Positive Number"
    elif n<0:
        return "Negtive Number"
    else:
        return "Zero"
    
print(checkNumber(233))
print(checkNumber(-33))
print(checkNumber(0))
print(checkNumber(0))
print(checkNumber(-234))
print(checkNumber(-0.21))
print(checkNumber(1))
print(checkNumber(9099))
print(checkNumber(-0))
