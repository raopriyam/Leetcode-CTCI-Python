# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 23:21:34 2021

@author: priya
"""

def sortDictByValues(dict1):
    for i in sorted(dict1.values()):
        print(i)
        
        
sortDictByValues({"a":1,"e":5,"d":4,"b":2,"c":3})