# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:04:10 2022

@author: priya
"""

def CheckBool(b1):
    if b1 == True or b1 == False:
        return "Boolean"
    else:
        return "Non boolean"
    
    
print(CheckBool(True))
print(CheckBool("True"))
print(CheckBool(123))