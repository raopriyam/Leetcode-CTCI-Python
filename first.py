# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:14:39 2023

@author: priya
"""

def first(arr,n):
    set1 = set(arr)
    return n in set1

print(first([1,2,3,4,5,6,9,8,7],33))