# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:05:00 2022

@author: priya
"""

def isunique1(s):
    set1 = set()
    for i in s:
        if i in set1:
            return False
        else:
            set1.add(i)
    return True
            
s = "PriyamA"
print(isunique1(s))