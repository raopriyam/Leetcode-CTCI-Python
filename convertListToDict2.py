# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:28:30 2021

@author: priya
"""

def convertListToDict2(arr1,arr2):
    dict1 = dict(zip(arr1,arr2))
    return dict1


print(convertListToDict2(["Nmae","Major"],["Priyam","IT"]))