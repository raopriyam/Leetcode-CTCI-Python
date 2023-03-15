# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 22:49:08 2023

@author: priya
"""

def checkPermutation(string1,string2):
    arr1 = list(string1)
    arr2 = list(string2)
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else: 
        return False
    

print(checkPermutation("Priyam", "mariP"))
    
    