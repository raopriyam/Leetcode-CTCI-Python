# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:16:41 2023

@author: priya
"""

def dictionary(arr1, arr2):
    check1 = 1
    check2 = -1
    dict1 = {}
    dict2 = {}
    for i in arr1:
        dict1[i] = check1
    for j in arr2:
        dict2[j] = check2
    return dict1, dict2
        
        
print(dictionary([1,2,3,4,5], ["a","b","c","d","e"]))
        
        