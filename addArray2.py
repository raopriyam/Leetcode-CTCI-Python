# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 23:08:33 2021

@author: priya
"""

def addArray2(arr1,arr2):
    num1 = ""
    num2 = ""
    for i in arr1:
        num1 = num1 + str(i)
    for i in arr2:
        num2 = num2 + str(i)
    num1 = str(int(num1) + int(num2))
    
    return list(num1)
    
    
    
print(addArray2([1,2,3],[4,5,6]))