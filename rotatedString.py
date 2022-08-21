# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:45:41 2022

@author: priya
"""

def rotatedString(s1,s2):
    sc = s2 + s2
    s1len = len(s1)
    for i in range(len(sc)):
        if i+s1len < len(sc):    
            if sc[i:i+s1len] == s1:
                return len(s1)-i
    return False
        
print(rotatedString("priyam","iyampr"))
