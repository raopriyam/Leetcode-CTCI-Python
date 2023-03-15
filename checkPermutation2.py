# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:05:03 2023

@author: priya
"""

def checkPermutation2(string1, string2):
    arr1 = [0]*26
    
    for i in string1:
        arr1[int(ord(i))-97] += 1 
        
    for j in string2:
        arr1[int(ord(j))-97] -= 1 
        
    if arr1 == [0]*26:
        return True
    
    return False
        
print(checkPermutation2("priyam", "myarip"))