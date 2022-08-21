# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:34:40 2022

@author: priya
"""

def stringRotate(s,k):
    a = s[:k]
    s1 = s[k:] + a
    return s1


print(stringRotate("PriyamRao",6))
    