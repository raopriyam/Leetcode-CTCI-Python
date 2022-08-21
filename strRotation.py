# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:58:08 2022

@author: priya
"""

def isSubstring(s1,s2):
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
    
def strRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    sc1 = s1 + s1 + s1
    sc2 = s2 + s2
    return isSubstring(sc1,sc2)

print(strRotation("Priyam","iyaPrm"))