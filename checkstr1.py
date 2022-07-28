# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:58:59 2022

@author: priya
"""

def checkstr(s1):
    if type(s1) == str:
        return "String"
    else:
        return "Non string"
    
    
print(checkstr("Priyam"))
print(checkstr(12345))
print(checkstr("Priyam"))
print(checkstr(True))

      
