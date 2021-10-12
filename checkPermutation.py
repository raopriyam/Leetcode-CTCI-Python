# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:14:27 2021

@author: priya
"""

def checkPermutation(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        a1 = list(s1)
        a2 = list(s2)
        a1.sort()
        a2.sort()
    if a1 == a2:
        return True
    return False

print(checkPermutation("Priyam","Priyam"))
print(checkPermutation("PriyaM","Priyam"))
print(checkPermutation("PrIYam","Priyam"))
print(checkPermutation("Priyamrao","Priyamrao"))
