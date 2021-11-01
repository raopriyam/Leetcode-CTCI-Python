# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:17:10 2021

@author: priya
"""

def arrCheck(arr1,arr2):
    dict1 = {}
    if len(arr1) < len(arr2):
        for i in arr2:
            if i not in dict1:
                dict1[i] = 1
        for j in arr1:
            if j not in dict1:
                return "Not Subset"
        return "Subset"
    else:
        for i in arr1:
            if i not in dict1:
                dict1[i] = 1
        for j in arr2:
            if j not in dict1:
                return "Not Subset"
        return "Subset"
        
        
print(arrCheck([1,2,3,4],[1,2,3,4,5]))