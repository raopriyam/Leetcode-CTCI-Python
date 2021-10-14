# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 11:57:14 2021

@author: priya
"""

def strRotate(s1,s2):
    if len(s1) != len(s2):
        return False
    
    else:
        s1 = s1 + s1
        if s2 in s1:
            return True
        else:
            return False
            
print(strRotate("priyam","riyamp"))
print(strRotate("priyamrao","raopriyam"))