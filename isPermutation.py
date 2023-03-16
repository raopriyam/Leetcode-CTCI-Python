# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:03:20 2023

@author: priya
"""

def isPermutation1(string1, string2):
    string1.replace(" ","")
    string2.replace(" ","")
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)

print(isPermutation1("driving", "crivign"))
        