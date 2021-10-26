# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 23:03:07 2021

@author: priya
"""

def addDict(dict1):
    for i in dict1:
        dict1[i] = dict1[i] + 1
        print(i,dict1[i])
        
dict1={1:1,2:2,3:3}
addDict(dict1)