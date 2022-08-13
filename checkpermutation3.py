# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:30:16 2022

@author: priya
"""

def checkpermutation(s1,s2):
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")
    if len(s1)!= len(s2):
        return False
    s1 = set(s1)
    for i in s2:
        if i not in s1:
            return False
    return True

print(checkpermutation("prRiyam","yamrip"))
    