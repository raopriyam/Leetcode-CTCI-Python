# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:18:11 2022

@author: priya
"""

def checkpermutation(s1,s2):
    if len(s1) != len(s2):
        return "not permutation"
    else:
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 == l2:
            return "permutation"
        else:
            return "not permutation"
        
        
s1 = "Priyam"
s2 = "riPma"
print(checkpermutation(s1,s2))