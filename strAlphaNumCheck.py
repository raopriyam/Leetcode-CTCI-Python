# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 22:10:44 2021

@author: priya
"""

def strcheck3(s):
    for i in s:
        if i>="0" and i<="9" or i>="A" and i<="z":
            pass
        else:
            return False
    return True


print(strcheck3("priyam"))
print(strcheck3("ra!o"))
print(strcheck3("12345#"))
print(strcheck3("priyamrao123"))
print(strcheck3("187426123"))


