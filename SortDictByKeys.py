# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:18:23 2021

@author: priya
"""

def sortDictByKeys(dict1):
    for i in sorted(dict1.keys()):
        print(i)
        
        
sortDictByKeys({"a":1,"e":5,"d":4,"b":2,"c":3})