# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:47:36 2021

@author: priya
"""

def addListInSet(arr):
    set1 = set()
    for i in arr:
        set1.add(i)
    return set1

print(addListInSet([1,2,3,4,5,6,7,8,9]))