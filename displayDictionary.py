# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 23:33:51 2023

@author: priya
"""

def displayDictionary(dict1):
    for i in dict1:
        if dict1[i] > 1:
            print(i,"=",dict1[i])
            
displayDictionary({"a":1,"b":2,"c":3})