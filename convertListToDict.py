# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:22:55 2021

@author: priya
"""

def convertListToDict(arr1,arr2):
    dict1 = {}
    for i in range(len(arr1)):
        dict1[arr1[i]] = arr2[i]
    return dict1 


print(convertListToDict(["Nmae","Major"],["Priyam","IT"]))