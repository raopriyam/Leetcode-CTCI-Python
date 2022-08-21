# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:49:41 2022

@author: priya
"""

def substring(s1,s2):
    lens1 = len(s1)
    lens2 = len(s2)
    if lens1>=lens2:
        if s2 in s1:
            return True
        return False
    else:
        if s1 in s2:
            return True
        return False 
    
print(substring("priyam","priyamr"))
    
    