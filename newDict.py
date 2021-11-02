# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:37:29 2021

@author: priya
"""

def newDict(arr1,dict1):
    dict2 = {}
    for i in arr1:
        dict2[i] = dict1[i]
    return dict2
        
print(newDict(["1"],{"1":1,"2":2}))