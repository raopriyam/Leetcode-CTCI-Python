# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:01:25 2021

@author: priya
"""

def editDict(dict1):
    for i in dict1:
        dict1[i] = dict1[i] +1
    return dict1
        
print(editDict({"1":1,"2":2,"3":3}))