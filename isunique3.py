# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:16:48 2022

@author: priya
"""

def isunique1(s):
    for i in s:
        if s.count(i)>1:
            return False
    return True
            
s = "Priyamrao"
print(isunique1(s))