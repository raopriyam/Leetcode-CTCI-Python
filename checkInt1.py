# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:02:06 2022

@author: priya
"""

def checkInt(i1):
    if type(i1) == int:
        return "Integer"
    else:
        return "Non Integer"
    
    
print(checkInt(12345))
print(checkInt(12345.34))
print(checkInt("Rao"))