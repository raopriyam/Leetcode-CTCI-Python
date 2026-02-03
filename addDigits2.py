# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 16:04:13 2026

@author: priya
"""

def addDigits( num: int) :
    while num>=10:
        num = sum(int(d) for d in str(num))
    return num
